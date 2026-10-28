#!/usr/bin/env python3
"""LeetCode practice tool: redo problems without seeing old answers, reveal hints layer by layer, archive attempts.

Run `python3 lc.py -h` for the command list.
"""

import argparse
import ast
import copy
import csv
import importlib.util
import itertools
import json
import re
import signal
import sys
import time
import traceback
import unicodedata
from datetime import date, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PROBLEMS = ROOT / "problems"
PRACTICE = ROOT / "practice"
STATE_FILE = PRACTICE / ".state.json"
HISTORY = ROOT / "history.csv"
REVIEW = ROOT / "REVIEW.md"

# Hint layers in reveal order; the layer after the last section prints the reference attempt.
HINT_SECTIONS = ["题型", "识别信号", "解题步骤", "关键一步"]
MAX_HINT = len(HINT_SECTIONS) + 1
REVIEW_SECTIONS = HINT_SECTIONS + ["易错点"]
CASE_TIMEOUT = 2.0  # seconds per sample case
BENCH_TIMEOUT = 3.0  # seconds for the large input
BASE_INTERVAL_DAYS = 3  # review interval after a non-clean attempt; doubles per consecutive clean attempt
HISTORY_FIELDS = ["date", "problem", "minutes", "hints", "optimal"]
VERSION_TABLE_HEADER = ["| 文件 | 思路 | 时间 | 空间 | 结论 |", "| --- | --- | --- | --- | --- |"]
PENDING = "待填"
TYPING_NAMES = {"List", "Optional", "Dict", "Set", "Tuple", "Deque"}
NODE_NAMES = {"ListNode", "TreeNode"}

sys.path.insert(0, str(ROOT))
sys.setrecursionlimit(10_000)

from helpers import linked_list_to_list, tree_to_list  # noqa: E402

NOTES_TEMPLATE = """\
# {title}

- 链接: {link}
- 难度: {pending}
- 最优解:

## 题型
{pending}

## 识别信号
{pending}

## 解题步骤
{pending}

## 关键一步
{pending}

## 各版本
{table}

## 易错点
{pending}
"""

CASES_TEMPLATE = """\
# 函数题: METHOD 填 Solution 里的方法名, CASES 每条写 dict(args=(参数, ...), expected=期望输出)。
# 设计题: 删掉 METHOD, 写 CLASS = "类名", CASES 每条写 dict(ops=[...], args=[[...], ...], expected=[...])。
# 可选: UNORDERED = True 忽略列表顺序; CHECK_ARG = 0 改为比较原地修改后的第 0 个参数;
#       def check(output, expected, args) 自定义比较（output 是原始返回值, args 是调用后的参数）;
#       def bench() 返回一组大输入参数, 用来比较各解法速度。
# 链表/树的参数用 helpers 里的 build_linked_list / build_tree 构造, 输出会自动转成 LeetCode 的列表写法。

METHOD = ""

CASES = [
    dict(args=(), expected=None),
]
"""

NEW_STUB = """
from typing import List, Optional


# 把 LeetCode 给的代码模板粘贴到这里, 并在 problems/{key}/cases.py 填好 METHOD 和样例
class Solution:
    pass
"""


class Timeout(BaseException):
    """Raised by the alarm; BaseException so a solution's `except Exception` cannot swallow it."""


class Problem:
    def __init__(self, path: Path):
        self.path = path
        self.key = path.name
        self.notes_path = path / "notes.md"
        self.cases_path = path / "cases.py"

    @property
    def ref(self) -> str:
        """What to type on the command line for this problem."""
        prefix = self.key.split("_", 1)[0]
        return str(int(prefix)) if prefix.isdigit() else self.key

    def notes(self) -> dict:
        return parse_notes(self.notes_path.read_text(encoding="utf-8"))

    def attempts(self) -> list:
        """Python attempts; these are the ones the tool runs."""
        return sorted((p for p in self.path.glob("*.py") if p.name != "cases.py"), key=attempt_sort_key)

    def dated_files(self) -> list:
        """Attempts in every language (Python, Java, JavaScript), named by date."""
        return sorted((p for p in self.path.iterdir() if attempt_date(p)), key=attempt_sort_key)

    def best_attempt(self):
        name = self.notes()["meta"].get("最优解", "")
        path = self.path / name if name else None
        return path if path and path.is_file() else None

    def reference_attempt(self):
        """Best attempt if the notes name a Python one, else the latest Python attempt."""
        best, attempts = self.best_attempt(), self.attempts()
        if best and best.suffix == ".py":
            return best
        return attempts[-1] if attempts else None


def die(message: str):
    print(message, file=sys.stderr)
    sys.exit(1)


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def attempt_date(path: Path):
    m = re.match(r"(\d{2})(\d{2})(\d{2})", path.stem)
    if not m:
        return None
    try:
        return date(2000 + int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


def attempt_sort_key(path: Path):
    m = re.fullmatch(r"(\d{6})(?:_(\d+))?", path.stem)
    return (m.group(1), int(m.group(2) or 1)) if m else (path.stem, 0)


def parse_notes(text: str) -> dict:
    title, meta, sections, current = "", {}, {}, None
    for line in text.splitlines():
        if line.startswith("## "):
            current = line[3:].strip()
            sections[current] = []
        elif current is not None:
            sections[current].append(line)
        elif line.startswith("# ") and not title:
            title = line[2:].strip()
        else:
            m = re.match(r"-\s*([^:：]+)[:：]\s*(.*)", line)
            if m:
                meta[m.group(1).strip()] = m.group(2).strip()
    return {
        "title": title,
        "meta": meta,
        "sections": {k: "\n".join(v).strip() for k, v in sections.items()},
    }


def version_rows(notes: dict) -> dict:
    """File name -> remaining cells of the 各版本 table."""
    rows = {}
    for line in notes["sections"].get("各版本", "").splitlines():
        cells = [c.strip().strip("`") for c in line.strip().strip("|").split("|")]
        if cells and cells[0].endswith(".py"):
            rows[cells[0]] = cells[1:]
    return rows


def all_problems() -> list:
    if not PROBLEMS.is_dir():
        return []
    return [Problem(p) for p in sorted(PROBLEMS.iterdir()) if (p / "notes.md").is_file()]


def find_problem(query: str) -> Problem:
    problems = all_problems()
    if query.isdigit():
        prefix = f"{int(query):04d}_"
        matches = [p for p in problems if p.key.startswith(prefix)]
    else:
        matches = [p for p in problems if slugify(query) in p.key]
    if not matches:
        die(f"找不到题目「{query}」。新题请用: python3 lc.py new \"42. Trapping Rain Water\"")
    if len(matches) > 1:
        die(f"「{query}」匹配到多道题: {', '.join(p.key for p in matches)}")
    return matches[0]


def practice_file(problem: Problem) -> Path:
    return PRACTICE / f"{problem.key}.py"


def load_state() -> dict:
    return json.loads(STATE_FILE.read_text()) if STATE_FILE.exists() else {}


def save_state(state: dict):
    PRACTICE.mkdir(exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, ensure_ascii=False, indent=2))


def practicing() -> list:
    return [Problem(PROBLEMS / p.stem) for p in sorted(PRACTICE.glob("*.py"))] if PRACTICE.is_dir() else []


def resolve_practice(query) -> Problem:
    """The problem being practiced; the id may be omitted when only one is in progress."""
    if query:
        problem = find_problem(query)
        if not practice_file(problem).exists():
            die(f"{problem.key} 不在练习区，先运行: python3 lc.py redo {problem.ref}")
        return problem
    current = practicing()
    if not current:
        die("练习区是空的，先运行 python3 lc.py redo <题号> 或 python3 lc.py new \"<题目>\"")
    if len(current) > 1:
        die(f"练习区里有 {len(current)} 道题，请指定题号: {', '.join(p.ref for p in current)}")
    return current[0]


_module_ids = itertools.count()


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location(f"_lc_{next(_module_ids)}", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def load_cases(problem: Problem):
    cases = load_module(problem.cases_path)
    if not getattr(cases, "CLASS", None) and not getattr(cases, "METHOD", None):
        die(f"{rel(problem.cases_path)} 里还没填 METHOD（函数题）或 CLASS（设计题）")
    if not getattr(cases, "CASES", None):
        die(f"{rel(problem.cases_path)} 里还没有样例")
    return cases


def case_args(case: dict, cases):
    return (case["ops"], case["args"]) if getattr(cases, "CLASS", None) else tuple(case["args"])


def _alarm(signum, frame):
    raise Timeout()


def call_with_timeout(fn, seconds: float):
    previous = signal.signal(signal.SIGALRM, _alarm)
    signal.setitimer(signal.ITIMER_REAL, seconds)
    try:
        return fn()
    finally:
        signal.setitimer(signal.ITIMER_REAL, 0)
        signal.signal(signal.SIGALRM, previous)


def run_target(module, cases, args):
    if getattr(cases, "CLASS", None):
        ops, op_args = args
        obj = getattr(module, cases.CLASS)(*op_args[0])
        return [None] + [getattr(obj, op)(*a) for op, a in zip(ops[1:], op_args[1:])]
    output = getattr(module.Solution(), cases.METHOD)(*args)
    check_arg = getattr(cases, "CHECK_ARG", None)
    return args[check_arg] if check_arg is not None else output


def normalize(value, unordered: bool):
    """Linked lists and trees become LeetCode list notation; with unordered, lists are sorted at every level."""
    if hasattr(value, "val") and hasattr(value, "next"):
        value = linked_list_to_list(value)
    elif hasattr(value, "val") and hasattr(value, "left") and hasattr(value, "right"):
        value = tree_to_list(value)
    if isinstance(value, (list, tuple)):
        items = [normalize(v, unordered) for v in value]
        return sorted(items, key=repr) if unordered else items
    return value


def equal(a, b) -> bool:
    if isinstance(a, float) or isinstance(b, float):
        return isinstance(a, (int, float)) and isinstance(b, (int, float)) and abs(a - b) <= 1e-5
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(equal(x, y) for x, y in zip(a, b))
    return a == b


def matches(output, expected, cases, args) -> bool:
    if hasattr(cases, "check"):
        return bool(cases.check(output, expected, args))
    unordered = getattr(cases, "UNORDERED", False)
    return equal(normalize(output, unordered), normalize(expected, unordered))


def short(value, limit: int = 80) -> str:
    text = repr(value)
    return text if len(text) <= limit else text[: limit - 3] + "..."


def describe_error(error: BaseException, path: Path) -> str:
    frames = [f for f in traceback.extract_tb(error.__traceback__) if f.filename == str(path)]
    where = f"（第 {frames[-1].lineno} 行）" if frames else ""
    return f"{type(error).__name__}: {error}{where}"


def run_bench(module, cases, path: Path) -> str:
    if not hasattr(cases, "bench"):
        return ""
    args = cases.bench()
    start = time.perf_counter()
    try:
        call_with_timeout(lambda: run_target(module, cases, args), BENCH_TIMEOUT)
    except Timeout:
        return f"超过 {BENCH_TIMEOUT:g}s"
    except Exception as e:
        return f"出错 {describe_error(e, path)}"
    return f"{(time.perf_counter() - start) * 1000:.1f}ms"


def test_attempt(path: Path, cases, verbose: bool = True) -> dict:
    """Runs the sample cases, then the large input if all pass; failures are always printed."""
    try:
        module = load_module(path)
    except Exception as e:
        print(f"  ✗ 文件无法运行: {describe_error(e, path)}")
        return {"ok": False, "passed": 0, "total": len(cases.CASES), "bench": ""}
    passed = 0
    for i, case in enumerate(cases.CASES, 1):
        args = copy.deepcopy(case_args(case, cases))
        start = time.perf_counter()
        try:
            output = call_with_timeout(lambda: run_target(module, cases, args), CASE_TIMEOUT)
            ok = matches(output, case["expected"], cases, args)
            detail = "" if ok else f"期望 {short(case['expected'])}，实际 {short(normalize(output, False))}"
        except Timeout:
            ok, detail = False, f"超过 {CASE_TIMEOUT:g}s"
        except Exception as e:
            ok, detail = False, describe_error(e, path)
        ms = (time.perf_counter() - start) * 1000
        if not ok:
            print(f"  ✗ 样例 {i}  输入 {short(case_args(case, cases))}  {detail}")
        elif verbose:
            print(f"  ✓ 样例 {i}  {ms:.2f}ms")
        passed += ok
    total = len(cases.CASES)
    bench = run_bench(module, cases, path) if passed == total else ""
    return {"ok": passed == total, "passed": passed, "total": total, "bench": bench}


def summary(result: dict) -> str:
    text = f"{result['passed']}/{result['total']} 通过"
    return text + (f"，大输入 {result['bench']}" if result["bench"] else "")


def practice_header(problem: Problem) -> list:
    notes = problem.notes()
    difficulty = notes["meta"].get("难度", "")
    title = notes["title"] + (f"  ({difficulty})" if difficulty and difficulty != PENDING else "")
    lines = [f"# {title}"]
    if notes["meta"].get("链接"):
        lines.append(f"# {notes['meta']['链接']}")
    r = problem.ref
    lines.append(f"# 测试: python3 lc.py test {r}    提示: python3 lc.py hint {r}    归档: python3 lc.py done {r}")
    return lines


def make_stub(problem: Problem) -> str:
    """Signature-only skeleton built from an archived attempt; no bodies, helpers or imports leak through."""
    source = problem.reference_attempt()
    if source is None:
        return NEW_STUB.format(key=problem.key)
    cases = load_cases(problem)
    class_name = getattr(cases, "CLASS", None) or "Solution"
    if getattr(cases, "CLASS", None):
        keep = {"__init__"} | {op for case in cases.CASES for op in case["ops"][1:]}
    else:
        keep = {cases.METHOD}
    stub = None
    for node in ast.parse(source.read_text(encoding="utf-8")).body:
        if isinstance(node, ast.ClassDef) and node.name == class_name:
            methods = [n for n in node.body if isinstance(n, ast.FunctionDef) and n.name in keep]
            for method in methods:
                method.body = [ast.Pass()]
                method.decorator_list = []
            node.body = methods or [ast.Pass()]
            node.decorator_list = []
            stub = node
            break
    if stub is None:
        die(f"{rel(source)} 里找不到 class {class_name}")
    names = {n.id for n in ast.walk(stub) if isinstance(n, ast.Name)}
    imports = []
    if names & TYPING_NAMES:
        imports.append(f"from typing import {', '.join(sorted(names & TYPING_NAMES))}")
    if names & NODE_NAMES:
        imports.append(f"from helpers import {', '.join(sorted(names & NODE_NAMES))}")
    head = "\n" + "\n".join(imports) + "\n\n\n" if imports else "\n"
    return head + re.sub(r"^(class .*:)\n\n", r"\1\n", ast.unparse(stub)) + "\n"


def start_practice(problem: Problem, body: str):
    PRACTICE.mkdir(exist_ok=True)
    path = practice_file(problem)
    path.write_text("\n".join(practice_header(problem)) + "\n" + body, encoding="utf-8")
    state = load_state()
    state[problem.key] = {"start": datetime.now().isoformat(timespec="seconds"), "hints": 0}
    save_state(state)
    print(f"已生成练习文件: {rel(path)}")
    print(f"写完运行 python3 lc.py test {problem.ref}；卡住了运行 python3 lc.py hint {problem.ref}")


def cmd_new(args):
    m = re.match(r"\s*(\d+)\s*[.、]?\s*(.+)", args.title)
    if m:
        number, name = int(m.group(1)), m.group(2).strip()
        key, title = f"{number:04d}_{slugify(name)}", f"{number}. {name}"
        link = f"https://leetcode.com/problems/{slugify(name).replace('_', '-')}/"
    else:
        key, title, link = slugify(args.title), args.title.strip(), ""
    folder = PROBLEMS / key
    if folder.exists():
        die(f"已经有这道题了，重做请用: python3 lc.py redo {Problem(folder).ref}")
    folder.mkdir(parents=True)
    table = "\n".join(VERSION_TABLE_HEADER)
    (folder / "notes.md").write_text(
        NOTES_TEMPLATE.format(title=title, link=link, pending=PENDING, table=table), encoding="utf-8"
    )
    (folder / "cases.py").write_text(CASES_TEMPLATE, encoding="utf-8")
    problem = Problem(folder)
    print(f"已建题目目录: {rel(folder)}（样例写在 cases.py，笔记写在 notes.md）")
    start_practice(problem, NEW_STUB.format(key=key))


def cmd_redo(args):
    problem = find_problem(args.problem)
    if practice_file(problem).exists():
        die(f"这道题已经在练习区: {rel(practice_file(problem))}")
    start_practice(problem, make_stub(problem))


def cmd_hint(args):
    problem = resolve_practice(args.problem)
    state = load_state()
    entry = state.setdefault(problem.key, {"start": datetime.now().isoformat(timespec="seconds"), "hints": 0})
    level = min(entry["hints"] + 1, MAX_HINT)
    entry["hints"] = level
    save_state(state)
    sections = problem.notes()["sections"]
    for i in range(1, level + 1):
        if i <= len(HINT_SECTIONS):
            name = HINT_SECTIONS[i - 1]
            print(f"── 提示 {i}/{MAX_HINT}  {name}")
            text = sections.get(name, "")
            print(text if text and text != PENDING else "（笔记里还没写）")
        else:
            dated = problem.dated_files()
            source = problem.best_attempt() or problem.reference_attempt() or (dated[-1] if dated else None)
            print(f"── 提示 {i}/{MAX_HINT}  旧答案 {source.name if source else ''}")
            print(source.read_text(encoding="utf-8").rstrip() if source else "（还没有归档的解答）")
        print()
    if level < MAX_HINT:
        upcoming = HINT_SECTIONS[level] if level < len(HINT_SECTIONS) else "旧答案"
        print(f"还卡住就再运行一次 hint，下一层是「{upcoming}」")


def cmd_test(args):
    problems = [resolve_practice(args.problem)] if args.problem else practicing()
    if not problems:
        resolve_practice(None)
    all_ok = True
    for problem in problems:
        path = practice_file(problem)
        cases = load_cases(problem)
        print(rel(path))
        result = test_attempt(path, cases)
        print(f"  {summary(result)}")
        all_ok &= result["ok"]
    return 0 if all_ok else 1


def cmd_check(args):
    problems = [find_problem(args.problem)] if args.problem else all_problems()
    failed = attempts = 0
    for problem in problems:
        cases = load_cases(problem)
        print(problem.key)
        for path in problem.attempts():
            print(f"  {path.name}")
            result = test_attempt(path, cases, verbose=False)
            print(f"    {summary(result)}")
            attempts += 1
            failed += not result["ok"]
    print(f"\n共 {len(problems)} 道题、{attempts} 份解答，{'全部通过' if not failed else f'{failed} 份未通过'}")
    return 1 if failed else 0


def pad(text: str, width: int) -> str:
    """Left-aligns text by terminal display width (CJK characters count as two columns)."""
    shown = sum(2 if unicodedata.east_asian_width(ch) in "WF" else 1 for ch in text)
    return text + " " * max(width - shown, 1)


def compare_attempts(problem: Problem, cases, current_result: dict):
    rows = version_rows(problem.notes())
    best = problem.best_attempt()
    print("\n各版本对比（大输入用时越短越好）:")
    for path in problem.attempts():
        result = test_attempt(path, cases, verbose=False)
        label = path.name + ("（最优解）" if best and path == best else "")
        idea = " | ".join(c for c in rows.get(path.name, []) if c and c != PENDING)
        print(f"  {pad(label, 22)}{pad(summary(result), 28)}{idea}")
    print(f"  {pad('本次', 22)}{summary(current_result)}")


def ask_optimal(flag) -> bool:
    if flag:
        return flag == "yes"
    if not sys.stdin.isatty():
        die("非交互环境请加 --optimal yes 或 --optimal no")
    while True:
        answer = input("这次是一步写出最优解吗？[y/n] ").strip().lower()
        if answer in ("y", "yes", "n", "no"):
            return answer.startswith("y")


def next_attempt_path(problem: Problem) -> Path:
    base = date.today().strftime("%y%m%d")
    path, n = problem.path / f"{base}.py", 2
    while path.exists():
        path, n = problem.path / f"{base}_{n}.py", n + 1
    return path


def strip_header(text: str, header: list) -> str:
    lines = text.splitlines()
    while lines and (lines[0] in header or not lines[0].strip()):
        lines.pop(0)
    return "\n".join(lines) + "\n"


def edit_notes(problem: Problem, attempt_name: str, set_best: bool):
    """Appends a 待填 row for the attempt to the 各版本 table and optionally records it as 最优解."""
    lines = problem.notes_path.read_text(encoding="utf-8").splitlines()
    row = f"| {attempt_name} | {PENDING} | {PENDING} | {PENDING} | {PENDING} |"
    try:
        start = lines.index("## 各版本")
    except ValueError:
        lines += ["", "## 各版本", *VERSION_TABLE_HEADER, row]
    else:
        end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith("## ")), len(lines))
        table_lines = [i for i in range(start + 1, end) if lines[i].startswith("|")]
        lines.insert(table_lines[-1] + 1 if table_lines else start + 1, row)
    if set_best:
        for i, line in enumerate(lines):
            if re.match(r"-\s*最优解[:：]", line):
                lines[i] = f"- 最优解: {attempt_name}"
                break
    problem.notes_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def read_history() -> list:
    if not HISTORY.exists():
        return []
    with HISTORY.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def append_history(row: dict):
    is_new = not HISTORY.exists()
    with HISTORY.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, HISTORY_FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(row)


def cmd_done(args):
    problem = resolve_practice(args.problem)
    path = practice_file(problem)
    cases = load_cases(problem)
    print(rel(path))
    result = test_attempt(path, cases)
    print(f"  {summary(result)}")
    if not result["ok"]:
        die("还没全部通过，修好再归档（卡住可以运行 hint）")
    compare_attempts(problem, cases, result)
    optimal = ask_optimal(args.optimal)

    state = load_state()
    entry = state.pop(problem.key, None) or {}
    minutes = ""
    if entry.get("start"):
        minutes = round((datetime.now() - datetime.fromisoformat(entry["start"])).total_seconds() / 60)
    dest = next_attempt_path(problem)
    dest.write_text(strip_header(path.read_text(encoding="utf-8"), practice_header(problem)), encoding="utf-8")
    path.unlink()
    save_state(state)
    hints = entry.get("hints", 0)
    append_history(
        {
            "date": date.today().isoformat(),
            "problem": problem.key,
            "minutes": minutes,
            "hints": hints,
            "optimal": "yes" if optimal else "no",
        }
    )
    edit_notes(problem, dest.name, set_best=optimal and problem.best_attempt() is None)

    print(f"\n已归档为 {rel(dest)}，用时 {minutes if minutes != '' else '?'} 分钟，用了 {hints} 层提示")
    sections = problem.notes()["sections"]
    print("\n── 对照笔记复盘 ──")
    for name in REVIEW_SECTIONS:
        print(f"[{name}]\n{sections.get(name) or PENDING}\n")
    print(f"记得在 {rel(problem.notes_path)} 的「各版本」表里补全 {dest.name} 这一行")


def cmd_next(args):
    by_problem = {}
    for row in read_history():
        by_problem.setdefault(row["problem"], []).append(row)
    today = date.today()
    ranked = []
    for problem in all_problems():
        records = by_problem.get(problem.key, [])
        if records:
            last = date.fromisoformat(records[-1]["date"])
        else:
            dates = [d for d in map(attempt_date, problem.dated_files()) if d]
            if not dates:
                continue
            last = max(dates)
        streak = 0
        for record in reversed(records):
            if record["hints"] != "0" or record["optimal"] != "yes":
                break
            streak += 1
        interval = BASE_INTERVAL_DAYS * 2**streak
        days = (today - last).days
        if not records:
            status = "还没重做过"
        elif streak:
            status = f"连续 {streak} 次不靠提示做出最优解"
        else:
            r = records[-1]
            status = f"上次用了 {r['hints']} 层提示" + ("" if r["optimal"] == "yes" else "，没做到最优")
        ranked.append((days / interval, problem, last, days, interval, status))
    ranked.sort(key=lambda item: item[0], reverse=True)
    due = sum(1 for item in ranked if item[0] >= 1)
    print(f"到期 {due} 道（共 {len(ranked)} 道）。最该重做的 {min(args.n, len(ranked))} 道:")
    for _, problem, last, days, interval, status in ranked[: args.n]:
        tags = problem.notes()["sections"].get("题型", "")
        print(f"  {problem.ref:>5}  {problem.notes()['title']}")
        print(f"         上次 {last}（{days} 天前，复习间隔 {interval} 天）· {status} · {tags}")


def one_line(text: str) -> str:
    parts = [re.sub(r"^\s*(?:[-*]|\d+\.)\s*", "", line).strip() for line in text.splitlines()]
    return "；".join(p for p in parts if p)


def cmd_index(args):
    groups = {}
    for problem in all_problems():
        notes = problem.notes()
        tags = [t.strip() for t in re.split(r"[·、,，/]", notes["sections"].get("题型", "")) if t.strip()]
        for tag in [t for t in tags if t != PENDING] or ["未分类"]:
            groups.setdefault(tag, []).append((problem, notes))
    lines = ["# 复习索引", "", "由 `python3 lc.py index` 根据各题 notes.md 生成，改笔记后重新运行即可。", ""]
    for tag in sorted(groups, key=lambda t: (-len(groups[t]), t)):
        lines += [f"## {tag}（{len(groups[tag])}）", ""]
        for problem, notes in groups[tag]:
            lines.append(f"- [{notes['title']}]({rel(problem.notes_path)})")
            for name in ("识别信号", "关键一步"):
                text = notes["sections"].get(name, "")
                if text and text != PENDING:
                    lines.append(f"  - {name}：{one_line(text)}")
        lines.append("")
    REVIEW.write_text("\n".join(lines), encoding="utf-8")
    print(f"已更新 {rel(REVIEW)}：{len(groups)} 个题型")


def main(argv=None):
    parser = argparse.ArgumentParser(description="LeetCode 刷题工具：盲做重做、分层提示、归档复盘。")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("new", help="新题：建题目目录并在练习区生成空白文件")
    p.add_argument("title", help='如 "42. Trapping Rain Water"')
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("redo", help="重做旧题：练习区只给函数签名，看不到旧答案")
    p.add_argument("problem", help="题号或题名片段")
    p.set_defaults(func=cmd_redo)

    p = sub.add_parser("hint", help="揭开下一层提示：题型 → 识别信号 → 解题步骤 → 关键一步 → 旧答案")
    p.add_argument("problem", nargs="?", help="练习区只有一道题时可省略")
    p.set_defaults(func=cmd_hint)

    p = sub.add_parser("test", help="测试练习区里的解答")
    p.add_argument("problem", nargs="?", help="省略则测试练习区全部题目")
    p.set_defaults(func=cmd_test)

    p = sub.add_parser("done", help="测试通过后归档，并与旧解法对比、对照笔记复盘")
    p.add_argument("problem", nargs="?", help="练习区只有一道题时可省略")
    p.add_argument("--optimal", choices=["yes", "no"], help="这次是否一步写出最优解；省略则交互询问")
    p.set_defaults(func=cmd_done)

    p = sub.add_parser("next", help="按复习间隔列出最该重做的题")
    p.add_argument("-n", type=int, default=10, help="列出几道，默认 10")
    p.set_defaults(func=cmd_next)

    p = sub.add_parser("check", help="用样例检查已归档的全部解答")
    p.add_argument("problem", nargs="?", help="省略则检查所有题目")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("index", help="根据各题笔记生成按题型分组的 REVIEW.md")
    p.set_defaults(func=cmd_index)

    args = parser.parse_args(argv)
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
