# LeetCode practice repo

In plain terms: this is the user's personal practice repo, driven by `python3 lc.py` (see README.md). Problems are solved blind in `practice/`; nothing about a problem's approach may be revealed while it is being solved.

## Recording mistakes from the current code

In plain terms: when the user asks to analyse their current code and record their mistakes (for example "帮我记错", "看看我这题错在哪，记进错题本"), find every concrete mistake in this attempt and file one mistake-notebook entry per mistake.

1. Find the problem: the `.py` file in `practice/`. With several, ask which one.
2. Read the attempt: the current code is `practice/<key>.py`. Earlier versions that failed a test are in `practice/.fails/<key>/<n>.py`, oldest first; mistakes already fixed there still count. Once the problem is archived, the current code is the newest dated file in `problems/<key>/` (failing versions remain until archiving finishes).
3. See how each version fails:
   - Current code: `python3 lc.py test <number>`.
   - Failing versions:

     ```bash
     python3 -c "import lc; p = lc.find_problem('<number>'); c = lc.load_cases(p); [print(f.name, lc.summary(lc.test_attempt(f, c))) for f in sorted((lc.FAILS / p.key).glob('*.py'), key=lambda f: int(f.stem))]"
     ```
4. For each distinct mistake, write a draft file in the scratchpad (layout below), then file it with `python3 lc.py oops <number> --file <draft>`. This writes `mistakes/<date>_<key>.md` and regenerates `MISTAKES.md`.
5. Open the new entries with `code <entry path>` so the user can adjust them, and tell the user in Chinese what was recorded.

Rules:

- Blind practice: while the problem is in `practice/`, do not read or quote its `notes.md` hint sections (题型, 识别信号, 解题步骤, 关键一步) or archived attempts, and do not describe the problem's approach or optimal solution. "正确写法" holds only the corrected lines of the user's own code.
- "错在哪" states the root cause in a sentence or two: the line, what was misused, and what it actually does. Symptoms, error messages and debugging detours stay out.
- Entries are written in Chinese. 类别 is exactly one of: Python 用法, 边界情况, 思路, 粗心.
- Never edit the user's practice file.

Draft layout (the same one the editor flow uses):

````markdown
# 记一个错：1. Two Sum

- 类别: Python 用法

## 错在哪

第 8 行用 `table[nums[i]]` 判断键是否存在；键不存在时直接抛 KeyError。

## 正确写法

```python
if nums[i] in table:
```

## 知识点

`dict[key]` 取不存在的键会抛 KeyError；判断存在用 `in`，取值带默认用 `get`。
````
