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
import os
import re
import signal
import subprocess
import sys
import textwrap
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
MISTAKES = ROOT / "mistakes.csv"
MISTAKES_PAGE = ROOT / "MISTAKES.md"
REVIEW = ROOT / "REVIEW.md"
PLANS = ROOT / "plans"
ROUND_FILE = ROOT / "round.json"
STATUS_MARK = {"round": "✓", "old": "○", "new": "·"}
STATUS_LEGEND = "✓ 本轮已做   ○ 以前做过、本轮还没做   · 从没做过"

# Hint layers in reveal order; the layer after the last section prints the reference attempt.
HINT_SECTIONS = ["题型", "识别信号", "解题步骤", "关键一步"]
MAX_HINT = len(HINT_SECTIONS) + 1
REVIEW_SECTIONS = HINT_SECTIONS + ["易错点"]
CASE_TIMEOUT = 2.0  # seconds per sample case
BENCH_TIMEOUT = 3.0  # seconds for the large input
BASE_INTERVAL_DAYS = 3  # review interval after a non-clean attempt; doubles per consecutive clean attempt
HISTORY_FIELDS = ["date", "problem", "minutes", "hints", "optimal"]
MISTAKE_FIELDS = ["date", "problem", "category", "mistake", "fix"]
# Mistake categories with the English name `-c` also accepts.
MISTAKE_CATEGORIES = {"Python 用法": "python", "边界情况": "edge", "思路": "idea", "粗心": "careless"}
VERSION_TABLE_HEADER = ["| 文件 | 思路 | 时间 | 空间 | 结论 |", "| --- | --- | --- | --- | --- |"]
PENDING = "待填"
DIFFICULTIES = {"Easy": "简单", "Medium": "中等", "Hard": "困难"}
UNRATED = "未标难度"
UNTAGGED = "未分类"
# English names for the 题型 tags, so `-t` accepts either language.
TAG_ENGLISH = {
    "哈希表": "hash table", "哈希计数": "hash counting", "双指针": "two pointers",
    "快慢指针": "fast and slow pointers", "滑动窗口": "sliding window", "前缀和": "prefix sum",
    "前后缀最大值": "prefix and suffix max", "二分查找": "binary search", "栈": "stack",
    "单调栈": "monotonic stack", "单调队列": "monotonic queue", "堆": "heap", "链表": "linked list",
    "二叉树": "binary tree", "二叉搜索树": "binary search tree", "递归": "recursion",
    "分治": "divide and conquer", "回溯": "backtracking", "DFS": "dfs", "BFS": "bfs", "图": "graph",
    "拓扑排序": "topological sort", "并查集": "union find", "字典树": "trie", "贪心": "greedy",
    "动态规划": "dynamic programming", "区间": "intervals", "排序": "sorting",
    "矩阵模拟": "matrix simulation", "字符串模拟": "string simulation", "数学": "math",
    "位运算": "bit manipulation", "设计": "design",
}
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

    @property
    def template(self) -> Path:
        """LeetCode's Python code template, used for the first attempt's stub."""
        return self.path / "template.py"

    def attempts(self) -> list:
        """Dated Python attempts; these are the ones the tool runs."""
        return sorted((p for p in self.path.glob("*.py") if attempt_date(p)), key=attempt_sort_key)

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


def error_trace(error: BaseException, path: Path) -> list:
    """The call chain inside the attempt file, outermost first: one line per frame with its source."""
    frames = [f for f in traceback.extract_tb(error.__traceback__) if f.filename == str(path)]
    return [f"第 {f.lineno} 行 {f.name}(): {f.line}" for f in frames]


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


def test_attempt(path: Path, cases, verbose: bool = True, details: bool = True) -> dict:
    """Runs the sample cases, then the large input if all pass; failures are always printed.

    With details off, a failure shows only its verdict (wrong answer, error, timeout), not the input, output or error.
    """
    try:
        module = load_module(path)
    except Exception as e:
        print(f"  ✗ 文件无法运行: {describe_error(e, path)}" if details else "  ✗ 文件无法运行（语法或导入出错）")
        return {"ok": False, "passed": 0, "total": len(cases.CASES), "bench": ""}
    passed = 0
    for i, case in enumerate(cases.CASES, 1):
        args = copy.deepcopy(case_args(case, cases))
        start = time.perf_counter()
        trace = []
        try:
            output = call_with_timeout(lambda: run_target(module, cases, args), CASE_TIMEOUT)
            ok = matches(output, case["expected"], cases, args)
            verdict = "答案不对"
            detail = "" if ok else f"期望 {short(case['expected'])}，实际 {short(normalize(output, False))}"
        except Timeout:
            ok, verdict, detail = False, "超时", f"超过 {CASE_TIMEOUT:g}s"
        except Exception as e:
            ok, verdict, detail = False, "运行出错", describe_error(e, path)
            trace = error_trace(e, path)
        ms = (time.perf_counter() - start) * 1000
        if not ok and not details:
            print(f"  ✗ 样例 {i}  {verdict}")
        elif not ok:
            print(f"  ✗ 样例 {i}  输入 {short(normalize(case_args(case, cases), False))}  {detail}")
            for line in trace:
                print(f"      {line}")
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


def custom_node_classes(tree: ast.Module) -> list:
    """Problem-specific node classes (e.g. graph or quad-tree Node), defined in code or in LeetCode's docstring."""
    def wanted(n):
        return isinstance(n, ast.ClassDef) and n.name.endswith("Node") and n.name not in NODE_NAMES

    found = []
    for node in tree.body:
        if wanted(node):
            found.append(node)
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Constant) and "class " in str(node.value.value):
            try:
                found += [n for n in ast.parse(textwrap.dedent(node.value.value)).body if wanted(n)]
            except SyntaxError:
                pass
    return found


def make_stub(problem: Problem) -> str:
    """Signature-only skeleton built from an archived attempt; no bodies, helpers or imports leak through."""
    source = problem.reference_attempt() or (problem.template if problem.template.exists() else None)
    if source is None:
        return NEW_STUB.format(key=problem.key)
    cases = load_cases(problem)
    class_name = getattr(cases, "CLASS", None) or "Solution"
    if getattr(cases, "CLASS", None):
        keep = {"__init__"} | {op for case in cases.CASES for op in case["ops"][1:]}
    else:
        keep = {cases.METHOD}
    stub = None
    tree = ast.parse(source.read_text(encoding="utf-8"))
    node_classes = custom_node_classes(tree)
    for node in tree.body:
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
    names = {n.id for c in node_classes + [stub] for n in ast.walk(c) if isinstance(n, ast.Name)}
    imports = []
    if names & TYPING_NAMES:
        imports.append(f"from typing import {', '.join(sorted(names & TYPING_NAMES))}")
    if names & NODE_NAMES:
        imports.append(f"from helpers import {', '.join(sorted(names & NODE_NAMES))}")
    head = "\n" + "\n".join(imports) + "\n\n\n" if imports else "\n"
    classes = [re.sub(r"^(class .*:)\n\n", r"\1\n", ast.unparse(c)) for c in node_classes + [stub]]
    return head + "\n\n\n".join(classes) + "\n"


def start_practice(problem: Problem, body: str):
    PRACTICE.mkdir(exist_ok=True)
    path = practice_file(problem)
    path.write_text("\n".join(practice_header(problem)) + "\n" + body, encoding="utf-8")
    state = load_state()
    state[problem.key] = {"start": datetime.now().isoformat(timespec="seconds"), "hints": 0}
    save_state(state)
    print(f"已生成练习文件: {rel(path)}")
    if not IN_MENU:
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
        again = "再选一次「要一层提示」" if IN_MENU else "再运行一次 hint"
        print(f"还卡住就{again}，下一层是「{upcoming}」")


def cmd_test(args):
    problems = [resolve_practice(args.problem)] if args.problem else practicing()
    if not problems:
        resolve_practice(None)
    all_ok = True
    for problem in problems:
        path = practice_file(problem)
        cases = load_cases(problem)
        print(rel(path))
        result = test_attempt(path, cases, details=not args.brief)
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
    if sys.stdin.isatty():
        print("\n这次还有要记进错题本的错吗？（直接回车跳过）")
        while prompt_mistake(problem):
            print("\n还有吗？（直接回车结束）")
    sections = problem.notes()["sections"]
    print("\n── 对照笔记复盘 ──")
    for name in REVIEW_SECTIONS:
        print(f"[{name}]\n{sections.get(name) or PENDING}\n")
    own = [m for m in read_mistakes() if m["problem"] == problem.key]
    if own:
        print("[错题本里这道题的记录]")
        for m in own:
            print(f"  {mistake_line(m)}")
        print()
    print(f"记得在 {rel(problem.notes_path)} 的「各版本」表里补全 {dest.name} 这一行")


def read_mistakes() -> list:
    if not MISTAKES.exists():
        return []
    with MISTAKES.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def wanted_category(value):
    """Maps a -c argument (Chinese or English, ignoring case) to a category name."""
    if value is None:
        return None
    wanted = re.sub(r"\s+", "", value).lower()
    for name, english in MISTAKE_CATEGORIES.items():
        if wanted in (re.sub(r"\s+", "", name).lower(), english):
            return name
    choices = " / ".join(f"{e}（{n}）" for n, e in MISTAKE_CATEGORIES.items())
    die(f"类别只能是 {choices}，收到「{value}」")


def mistake_line(m: dict, with_category: bool = True) -> str:
    fix = f"  →  {m['fix']}" if m["fix"] else ""
    tag = f"[{m['category']}] " if with_category else ""
    return f"{m['date']}  {tag}{m['mistake']}{fix}"


def problem_title(key: str) -> str:
    problem = Problem(PROBLEMS / key)
    return problem.notes()["title"] if problem.notes_path.exists() else key


def table_cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ") or "—"


def write_mistakes_page(mistakes: list):
    """Regenerates MISTAKES.md from mistakes.csv, grouped by category, newest first."""
    lines = ["# 错题本", "", "由 `python3 lc.py oops` 记录（数据在 mistakes.csv），每记一条自动重新生成。", ""]
    for category in MISTAKE_CATEGORIES:
        rows = [m for m in reversed(mistakes) if m["category"] == category]
        if not rows:
            continue
        lines += [f"## {category}（{len(rows)}）", "", "| 日期 | 题目 | 错在哪 | 正确写法 |", "| --- | --- | --- | --- |"]
        for m in rows:
            problem = PROBLEMS / m["problem"] / "notes.md"
            link = f"[{problem_title(m['problem'])}]({rel(problem)})" if problem.exists() else m["problem"]
            lines.append(f"| {m['date']} | {link} | {table_cell(m['mistake'])} | {table_cell(m['fix'])} |")
        lines.append("")
    MISTAKES_PAGE.write_text("\n".join(lines), encoding="utf-8")


def record_mistake(problem: Problem, category: str, mistake: str, fix: str):
    is_new = not MISTAKES.exists()
    with MISTAKES.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, MISTAKE_FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow({"date": date.today().isoformat(), "problem": problem.key,
                         "category": category, "mistake": mistake, "fix": fix})
    write_mistakes_page(read_mistakes())
    print(f"已记进错题本（{category}）：{mistake}")


def prompt_mistake(problem: Problem, mistake: str = "") -> bool:
    """Asks for one mistake interactively; returns False when the answer is left empty."""
    try:
        mistake = mistake or input("错在哪: ").strip()
        if not mistake:
            return False
        fix = input("正确写法（可留空）: ").strip()
        names = list(MISTAKE_CATEGORIES)
        print("类别: " + "   ".join(f"{i}. {n}" for i, n in enumerate(names, 1)))
        while True:
            answer = input("选择编号: ").strip()
            if answer.isdigit() and 1 <= int(answer) <= len(names):
                break
            print("  没有这个编号，再选一次")
    except (EOFError, KeyboardInterrupt):
        print()
        return False
    record_mistake(problem, names[int(answer) - 1], mistake, fix)
    return True


def cmd_oops(args):
    problem = find_problem(args.problem) if args.problem else resolve_practice(None)
    category = wanted_category(args.c)
    if args.m and category:
        record_mistake(problem, category, args.m.strip(), (args.f or "").strip())
        return
    if not sys.stdin.isatty():
        die("非交互环境请同时给出 -m 错在哪 和 -c 类别")
    print(f"记一个错：{problem.notes()['title']}")
    prompt_mistake(problem, (args.m or "").strip())


def cmd_mistakes(args):
    category = wanted_category(args.c)
    key = find_problem(args.problem).key if args.problem else None
    mistakes = [m for m in read_mistakes()
                if (not key or m["problem"] == key) and (not category or m["category"] == category)]
    if not mistakes:
        print("错题本里还没有符合条件的记录。做题时发现错误可以运行: python3 lc.py oops")
        return
    for name in MISTAKE_CATEGORIES:
        rows = [m for m in reversed(mistakes) if m["category"] == name]
        if not rows:
            continue
        print(f"\n── {name}（{len(rows)}）")
        for m in rows:
            print(f"  {problem_title(m['problem'])}")
            print(f"    {mistake_line(m, with_category=False)}")
    print(f"\n共 {len(mistakes)} 条；也可以直接打开 {rel(MISTAKES_PAGE)} 看")


def problem_tags(notes: dict) -> list:
    tags = [t.strip() for t in re.split(r"[·、,，/]", notes["sections"].get("题型", "")) if t.strip()]
    return [t for t in tags if t != PENDING]


def problem_difficulty(notes: dict) -> str:
    value = notes["meta"].get("难度", "").strip().title()
    return value if value in DIFFICULTIES else UNRATED


def wanted_difficulty(value):
    """Maps an -d argument (English or Chinese) to Easy / Medium / Hard."""
    if value is None:
        return None
    for name, label in DIFFICULTIES.items():
        if value.strip().lower() in (name.lower(), label):
            return name
    die(f"难度只能是 easy / medium / hard（或 简单 / 中等 / 困难），收到「{value}」")


EXACT_TAG_NAMES = {t.lower() for t in TAG_ENGLISH} | set(TAG_ENGLISH.values())


def tag_matches(tag: str, query: str) -> bool:
    """A full tag name (Chinese or English) matches only that tag; anything else matches by substring, ignoring case."""
    query = query.strip().lower()
    names = {tag.lower(), TAG_ENGLISH.get(tag, "")} - {""}
    if query in EXACT_TAG_NAMES:
        return query in names
    return any(query in name for name in names)


def passes_filters(notes: dict, difficulty, tag) -> bool:
    if difficulty and problem_difficulty(notes) != difficulty:
        return False
    return not tag or any(tag_matches(t, tag) for t in problem_tags(notes))


def cmd_next(args):
    difficulty = wanted_difficulty(args.d)
    by_problem = {}
    for row in read_history():
        by_problem.setdefault(row["problem"], []).append(row)
    today = date.today()
    ranked = []
    for problem in all_problems():
        if not passes_filters(problem.notes(), difficulty, args.t):
            continue
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
        for tag in problem_tags(notes) or [UNTAGGED]:
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


def round_start():
    """Start date of the current practice round, or None when no round has been started."""
    if not ROUND_FILE.exists():
        return None
    return date.fromisoformat(json.loads(ROUND_FILE.read_text(encoding="utf-8"))["start"])


def problem_status(problem: Problem, start) -> str:
    """'round' if an attempt was archived on or after the round start, 'old' if only before it, else 'new'.

    Without a round, any archived attempt counts as 'round'.
    """
    dates = [d for d in map(attempt_date, problem.dated_files()) if d]
    if any(start is None or d >= start for d in dates):
        return "round"
    return "old" if dates else "new"


def round_summary(start) -> str:
    if start is None:
        return "本轮: 还没开始（在菜单里选「开始新一轮」）"
    done = sum(problem_status(p, start) == "round" for p in all_problems())
    return f"本轮: {start} 开始，已做 {done} 道"


def cmd_round(args):
    if args.new:
        ROUND_FILE.write_text(json.dumps({"start": date.today().isoformat()}) + "\n", encoding="utf-8")
        print(f"已开始新一轮: {date.today()}。之前做过的题都标成「以前做过」，会重新出现在 list 和刷题菜单里")
    print(round_summary(round_start()))
    return 0


def cmd_list(args):
    difficulty = wanted_difficulty(args.d)
    start = round_start()
    plan_ids = None
    if args.plan:
        plans = [p for p in load_plans() if args.plan.lower() in p["slug"] or args.plan.lower() in p["name"].lower()]
        if len(plans) != 1:
            die(f"「{args.plan}」匹配到 {len(plans)} 个题单: {', '.join(p['slug'] for p in load_plans())}")
        plan_ids = {str(q["id"]) for g in plans[0]["groups"] for q in g["problems"]}
    groups = {}  # difficulty -> tag -> [(problem, notes, status)]
    hidden = set()
    for problem in all_problems():
        notes = problem.notes()
        if plan_ids is not None and problem.ref not in plan_ids:
            continue
        if not passes_filters(notes, difficulty, args.t):
            continue
        status = problem_status(problem, start)
        if status == "round" and not args.all:
            hidden.add(problem.key)
            continue
        tags = [t for t in problem_tags(notes) if not args.t or tag_matches(t, args.t)] or [UNTAGGED]
        for tag in tags:
            groups.setdefault(problem_difficulty(notes), {}).setdefault(tag, []).append((problem, notes, status))
    for level in [*DIFFICULTIES, UNRATED]:
        by_tag = groups.get(level)
        if not by_tag:
            continue
        distinct = {p.key for rows in by_tag.values() for p, _, _ in rows}
        label = f"{DIFFICULTIES[level]} {level}" if level in DIFFICULTIES else level
        print(f"\n{label}（{len(distinct)} 道）")
        for tag in sorted(by_tag, key=lambda t: (-len(by_tag[t]), t)):
            print(f"  {tag}（{len(by_tag[tag])}）")
            for problem, notes, status in by_tag[tag]:
                print(f"    {STATUS_MARK[status]} {problem.ref:>5}  {notes['title'].split('. ', 1)[-1]}")
    if not groups:
        print("没有符合条件的题")
    if hidden:
        print(f"\n本轮已做的 {len(hidden)} 道没有列出（加 --all 显示）")
    print(f"\n{STATUS_LEGEND}。一道题有多个题型时，会在每个题型下各出现一次。开始一道题: python3 lc.py start <题号>")
    return 0


def load_plans() -> list:
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(PLANS.glob("*.json"))] if PLANS.is_dir() else []


def cmd_plan(args):
    plans = load_plans()
    if not plans:
        die("plans/ 里还没有题单")
    solved = {p.ref for p in all_problems() if p.dated_files()}
    if not args.name:
        for plan in plans:
            ids = [str(q["id"]) for g in plan["groups"] for q in g["problems"]]
            print(f"{plan['name']}: 已做 {sum(i in solved for i in ids)}/{len(ids)}    python3 lc.py plan {plan['slug']}")
        return 0
    matches = [p for p in plans if args.name.lower() in p["slug"] or args.name.lower() in p["name"].lower()]
    if len(matches) != 1:
        die(f"「{args.name}」匹配到 {len(matches)} 个题单: {', '.join(p['slug'] for p in plans)}")
    plan = matches[0]
    total = done = 0
    for group in plan["groups"]:
        problems = group["problems"]
        group_done = sum(str(q["id"]) in solved for q in problems)
        total, done = total + len(problems), done + group_done
        print(f"{group['name']}  {group_done}/{len(problems)}")
        for q in problems:
            is_done = str(q["id"]) in solved
            if args.all or not is_done:
                print(f"  {'✓' if is_done else '·'} {q['id']:>5}  {q['title']}  ({q['difficulty']})")
    print(f"\n{plan['name']}: 已做 {done}/{total}。开始一道题: python3 lc.py start <题号>")
    return 0


ALIAS_COMMENT = "# LeetCode practice menu (added by `python3 lc.py setup`)"
GIT_NAME = "Renee Lu"
GIT_EMAIL = "reneelu419@gmail.com"


def shell_rc_file():
    """The startup file of the user's login shell, or None when the shell is not zsh or bash."""
    shell = Path(os.environ.get("SHELL", "")).name
    home = Path.home()
    if shell == "zsh":
        return home / ".zshrc"
    if shell == "bash":
        return home / (".bash_profile" if sys.platform == "darwin" else ".bashrc")
    return None


def setup_git_signing() -> int:
    """Repo-local commit identity and SSH signing with the celestia key, so commits never use a global work identity."""
    key = Path.home() / ".ssh" / "id_celestia.pub"
    if not key.exists():
        print(f"没找到 {key}：先把 celestia 的 SSH key 放到 ~/.ssh/ 再运行 setup，否则提交会用全局的 git 身份")
        return 1
    signers = ROOT / ".git" / "allowed_signers"
    signers.write_text(f"{GIT_EMAIL} {key.read_text().strip()}\n", encoding="utf-8")
    settings = {
        "user.name": GIT_NAME, "user.email": GIT_EMAIL, "gpg.format": "ssh", "user.signingkey": str(key),
        "commit.gpgsign": "true", "gpg.ssh.allowedSignersFile": str(signers),
    }
    for name, value in settings.items():
        subprocess.run(["git", "-C", str(ROOT), "config", "--local", name, value], check=True)
    print(f"已设置本仓库的 git 身份: {GIT_NAME} <{GIT_EMAIL}>，提交用 {key.name} 签名")
    return 0


def cmd_setup(args):
    git_result = setup_git_signing()
    alias = f'alias lc="python3 {ROOT / "lc.py"}"'
    rc = shell_rc_file()
    if rc is None:
        print(f"没认出你的 shell（$SHELL={os.environ.get('SHELL', '')}），请把这一行加进它的启动文件:\n{alias}")
        return 1
    lines = rc.read_text(encoding="utf-8").splitlines() if rc.exists() else []
    existing = [i for i, line in enumerate(lines) if re.match(r"\s*alias lc=", line)]
    ours = [i for i in existing if "lc.py" in lines[i]]
    if existing and not ours:
        print(f"{rc} 里已经有一个别的 lc 别名: {lines[existing[0]].strip()}\n没有改动；想换成这个工具的话，把那行改成:\n{alias}")
        return 1
    if ours and lines[ours[0]].strip() == alias:
        print(f"{rc} 里已经配好了: {alias}")
        return git_result
    if ours:
        lines[ours[0]] = alias
        action = "已更新"
    else:
        lines += ["", ALIAS_COMMENT, alias]
        action = "已添加"
    rc.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"{action} {rc}: {alias}\n新开一个终端，或运行 source {rc}，然后输入 lc 即可")
    return git_result


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="LeetCode 刷题工具：盲做重做、分层提示、归档复盘。不带参数运行则进入菜单。")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("new", help="新题：建题目目录并在练习区生成空白文件")
    p.add_argument("title", help='如 "42. Trapping Rain Water"')
    p.set_defaults(func=cmd_new)

    p = sub.add_parser("redo", aliases=["start"], help="开始做一道已建好的题（新题或重做）：练习区只给函数签名")
    p.add_argument("problem", help="题号或题名片段")
    p.set_defaults(func=cmd_redo)

    p = sub.add_parser("hint", help="揭开下一层提示：题型 → 识别信号 → 解题步骤 → 关键一步 → 旧答案")
    p.add_argument("problem", nargs="?", help="练习区只有一道题时可省略")
    p.set_defaults(func=cmd_hint)

    p = sub.add_parser("test", help="测试练习区里的解答")
    p.add_argument("problem", nargs="?", help="省略则测试练习区全部题目")
    p.add_argument("--brief", action="store_true", help="没通过的样例只说是答案不对、运行出错还是超时，不显示输入、输出和报错")
    p.set_defaults(func=cmd_test)

    p = sub.add_parser("done", help="测试通过后归档，并与旧解法对比、对照笔记复盘")
    p.add_argument("problem", nargs="?", help="练习区只有一道题时可省略")
    p.add_argument("--optimal", choices=["yes", "no"], help="这次是否一步写出最优解；省略则交互询问")
    p.set_defaults(func=cmd_done)

    categories = " / ".join(f"{e}（{n}）" for n, e in MISTAKE_CATEGORIES.items())
    p = sub.add_parser("oops", help="记一个错进错题本；不给 -m / -c 就逐项询问")
    p.add_argument("problem", nargs="?", help="省略则记在练习区唯一那道题上")
    p.add_argument("-m", metavar="错在哪", help="犯了什么错")
    p.add_argument("-f", metavar="正确写法", help="应该怎么写（可省略）")
    p.add_argument("-c", metavar="类别", help=f"类别：{categories}")
    p.set_defaults(func=cmd_oops)

    p = sub.add_parser("mistakes", help="翻错题本：按类别列出记过的错，最新的在前")
    p.add_argument("problem", nargs="?", help="只看某道题")
    p.add_argument("-c", metavar="类别", help=f"只看某个类别：{categories}")
    p.set_defaults(func=cmd_mistakes)

    p = sub.add_parser("next", help="按复习间隔列出最该重做的题")
    p.add_argument("-n", type=int, default=10, help="列出几道，默认 10")
    p.add_argument("-d", metavar="难度", help="只看某个难度：easy / medium / hard（或 简单 / 中等 / 困难）")
    p.add_argument("-t", metavar="题型", help="只看某个题型，中英文都行（如 双指针 或 two pointers）；按包含匹配，tree 会同时匹配 二叉树 和 二叉搜索树")
    p.set_defaults(func=cmd_next)

    p = sub.add_parser("round", help="看本轮进度；加 --new 开始新一轮")
    p.add_argument("--new", action="store_true", help="从今天开始新一轮")
    p.set_defaults(func=cmd_round)

    p = sub.add_parser("list", help="按难度、再按题型分组列出本轮还没做的题（新题和以前做过的都在）")
    p.add_argument("-d", metavar="难度", help="只看某个难度：easy / medium / hard（或 简单 / 中等 / 困难）")
    p.add_argument("-t", metavar="题型", help="只看某个题型，中英文都行；按包含匹配")
    p.add_argument("--plan", metavar="题单", help="只看某个题单里的题，如 top")
    p.add_argument("--all", action="store_true", help="本轮已做的题也列出来（打 ✓）")
    p.set_defaults(func=cmd_list)

    p = sub.add_parser("check", help="用样例检查已归档的全部解答")
    p.add_argument("problem", nargs="?", help="省略则检查所有题目")
    p.set_defaults(func=cmd_check)

    p = sub.add_parser("index", help="根据各题笔记生成按题型分组的 REVIEW.md")
    p.set_defaults(func=cmd_index)

    p = sub.add_parser("setup", help="新电脑上 clone 之后运行一次：配好 lc 别名，以及本仓库的 git 身份和 celestia 签名")
    p.set_defaults(func=cmd_setup)

    p = sub.add_parser("plan", help="题单进度：按分组列出还没做的题")
    p.add_argument("name", nargs="?", help="题单名片段；省略则列出所有题单的进度")
    p.add_argument("--all", action="store_true", help="已做的题也列出来")
    p.set_defaults(func=cmd_plan)

    return parser


def run(argv: list) -> int:
    """Runs one command; errors that would exit the program return their exit code instead."""
    try:
        args = build_parser().parse_args(argv)
        return args.func(args) or 0
    except SystemExit as e:
        return e.code if isinstance(e.code, int) else 1


IN_MENU = False  # set while the interactive menu runs, so commands can leave out command-line instructions


class MenuExit(Exception):
    """Raised on 0, Ctrl-D or Ctrl-C to leave the menu."""


def ask(prompt: str) -> str:
    try:
        return input(prompt).strip()
    except (EOFError, KeyboardInterrupt):
        print()
        raise MenuExit()


def choose(title: str, options: list, allow_all: bool = True):
    """Numbered pick from options [(label, value)]; Enter means all (None) when allowed."""
    print(f"\n{title}:")
    for i, (label, _) in enumerate(options, 1):
        print(f"  {i:>2}. {label}")
    hint = "（回车 = 全部）" if allow_all else ""
    while True:
        answer = ask(f"选择编号{hint}: ")
        if not answer and allow_all:
            return None
        if answer.isdigit() and 1 <= int(answer) <= len(options):
            return options[int(answer) - 1][1]
        print("  没有这个编号，再选一次")


def round_tag_counts(difficulty) -> list:
    """[(tag, done this round, total)] for the difficulty, most remaining first."""
    start, counts = round_start(), {}
    for problem in all_problems():
        notes = problem.notes()
        if not passes_filters(notes, difficulty, None):
            continue
        done = problem_status(problem, start) == "round"
        for tag in problem_tags(notes) or [UNTAGGED]:
            pair = counts.setdefault(tag, [0, 0])
            pair[0] += done
            pair[1] += 1
    return sorted(((t, d, n) for t, (d, n) in counts.items()), key=lambda x: (-(x[2] - x[1]), x[0]))


def offer_start() -> bool:
    answer = ask("\n输入题号开始做（回车返回菜单）: ")
    return bool(answer) and start_and_practice(answer)


def start_and_practice(query: str) -> bool:
    """Starts the problem unless it is already in the practice area, then opens its practice menu; True if opened."""
    try:
        problem = find_problem(query)
    except SystemExit:
        return False
    if practice_file(problem).exists():
        print("这道题已经在练习区，接着做")
    elif run(["start", problem.ref]) != 0:
        return False
    practice_menu(problem)
    return True


def practice_menu(problem: Problem):
    """Test / hint / mistake / archive loop for one problem; leaves once it is archived or on 0."""
    ref = problem.ref
    actions = [
        ("测试（没通过的只说答案不对 / 运行出错 / 超时）", ["test", ref, "--brief"]),
        ("测试（显示输入、期望输出、实际输出和报错位置）", ["test", ref]),
        ("要一层提示", ["hint", ref]),
        ("记一个错进错题本", ["oops", ref]),
        ("归档并复盘", ["done", ref]),
    ]
    while practice_file(problem).exists():
        entry = load_state().get(problem.key, {})
        minutes = ""
        if entry.get("start"):
            minutes = f"，已做 {round((datetime.now() - datetime.fromisoformat(entry['start'])).total_seconds() / 60)} 分钟"
        print(f"\n── 正在做 {problem.notes()['title']}（已用 {entry.get('hints', 0)} 层提示{minutes}）")
        print(f"   在编辑器里改 {rel(practice_file(problem))}，然后在这里选:")
        for i, (label, _) in enumerate(actions, 1):
            print(f"  {i}. {label}")
        print("  0. 回主菜单（练习文件留着，之后可以接着做）")
        answer = ask("选择编号: ")
        if answer == "0":
            return
        if not answer.isdigit() or not 1 <= int(answer) <= len(actions):
            print("没有这个编号")
            continue
        print()
        run(actions[int(answer) - 1][1])


def choose_difficulty():
    return choose("难度", [(f"{label} {name}", name.lower()) for name, label in DIFFICULTIES.items()])


def menu_practice():
    difficulty = choose_difficulty()
    counts = round_tag_counts(wanted_difficulty(difficulty))
    if not counts:
        print("这个难度下没有题")
        return
    tag = choose("题型（括号里是本轮已做 / 总数）", [(f"{t}（{d}/{n}）", t) for t, d, n in counts])
    run(["list"] + (["-d", difficulty] if difficulty else []) + (["-t", tag] if tag else []))
    return offer_start()


def menu_new_round():
    print(round_summary(round_start()))
    if ask("开始新一轮？之前做过的题会重新算作本轮没做 [y/N]: ").lower() in ("y", "yes"):
        run(["round", "--new"])


def menu_start():
    answer = ask("题号或题名片段: ")
    return bool(answer) and start_and_practice(answer)


def menu_continue():
    current = practicing()
    if not current:
        print("练习区是空的，先选一道题开始做")
        return
    target = current[0] if len(current) == 1 else choose(
        "练习区里有几道题，选一道", [(p.notes()["title"], p) for p in current], allow_all=False)
    practice_menu(target)
    return True


def menu_oops():
    current = practicing()
    default = f"，回车 = {current[0].notes()['title']}" if len(current) == 1 else ""
    answer = ask(f"记在哪道题上（题号或题名片段{default}）: ")
    if answer or default:
        run(["oops", answer or current[0].ref])


def menu_mistakes():
    category = choose("类别", [(name, name) for name in MISTAKE_CATEGORIES])
    run(["mistakes"] + (["-c", category] if category else []))


def menu_next():
    difficulty = choose_difficulty()
    tag = ask("题型（中英文都行，回车 = 全部）: ")
    run(["next"] + (["-d", difficulty] if difficulty else []) + (["-t", tag] if tag else []))
    return offer_start()


def menu_plan():
    plans = load_plans()
    if not plans:
        print("plans/ 里还没有题单")
        return
    slug = plans[0]["slug"] if len(plans) == 1 else choose(
        "题单", [(p["name"], p["slug"]) for p in plans], allow_all=False)
    run(["plan", slug])
    return offer_start()


def menu_new():
    title = ask('题目（如 "42. Trapping Rain Water"）: ')
    if not title:
        return
    before = {p.key for p in practicing()}
    if run(["new", title]) == 0:
        added = [p for p in practicing() if p.key not in before]
        if added:
            practice_menu(added[0])
            return True
    return False


# Each action returns True when it ended in the practice menu, which needs no extra "press Enter" pause.
MENU = [
    ("刷题：按难度 → 题型选（新题和做过的题都在，本轮做过的不列）", menu_practice),
    ("开始做指定的题（输入题号）", menu_start),
    ("接着做练习区里的题（测试 / 提示 / 记错 / 归档）", menu_continue),
    ("记一个错进错题本", menu_oops),
    ("翻错题本", menu_mistakes),
    ("复习：按遗忘间隔排出最该重做的题", menu_next),
    ("题单进度", menu_plan),
    ("开始新一轮", menu_new_round),
    ("新建题单以外的题", menu_new),
    ("检查全部已归档的解答", lambda: run(["check"])),
    ("重新生成复习索引 REVIEW.md", lambda: run(["index"])),
]


def menu():
    global IN_MENU
    IN_MENU = True
    try:
        if practicing():
            menu_continue()
        while True:
            state = load_state()
            current = practicing()
            print("\n══ LeetCode 刷题 ══")
            print(round_summary(round_start()))
            if current:
                for p in current:
                    hints = state.get(p.key, {}).get("hints", 0)
                    print(f"练习区: {p.notes()['title']}（已用 {hints} 层提示）  {rel(practice_file(p))}")
            else:
                print("练习区: 空")
            for i, (label, _) in enumerate(MENU, 1):
                print(f"  {i:>2}. {label}")
            print("   0. 退出")
            answer = ask("选择编号: ")
            if answer == "0":
                return
            if not answer.isdigit() or not 1 <= int(answer) <= len(MENU):
                print("没有这个编号")
                continue
            if not MENU[int(answer) - 1][1]():
                ask("\n回车返回菜单")
    except MenuExit:
        return


def main(argv=None):
    argv = sys.argv[1:] if argv is None else argv
    if not argv:
        menu()
        return
    sys.exit(run(argv))


if __name__ == "__main__":
    main()
