# LeetCode Practice

In plain terms: every problem lives in its own folder with its test cases, study notes and every past attempt. Solving or redoing a problem happens in a separate practice area that shows only the function signature, so old answers stay out of sight until the new attempt passes and is archived. Problems from a list that have not been solved yet already have their folder, official examples and notes, so the hint layers work on the first attempt too.

Requires Python 3.10+, standard library only.

## Menu

In plain terms: run the tool with no arguments to get a numbered menu; each entry asks for what it needs, so no command has to be remembered.

```bash
python3 lc.py     # or just `lc`, with this line in ~/.zshrc:
                  # alias lc="python3 /Users/renee.lu/Project/leetcode/lc.py"
```

The menu shows what is in the practice area and offers: pick a new problem by difficulty and then type, start a problem, test, hint, archive, problems due for a redo, list progress, add a problem outside the lists, check every archived attempt, and rebuild `REVIEW.md`. Picking a new problem, the redo list and list progress each end by asking for a problem number to start right away. `0`, Ctrl-D or Ctrl-C leaves the menu.

## Daily loop

In plain terms: pick a problem that is due, solve it blind, reveal hints only when stuck, then archive it and compare with past attempts. Every menu entry is one of these commands, which also work directly.

```bash
python3 lc.py list -d medium -t tree   # unsolved problems by difficulty, then by type
python3 lc.py next -d easy             # problems most due for a redo
python3 lc.py plan top                 # problems in a list that are not done yet
python3 lc.py start 42                 # blank practice file: signature only (same as redo)
python3 lc.py test                     # sample cases, then a large input for speed
python3 lc.py hint                     # reveal the next hint layer
python3 lc.py done                     # archive, compare with past attempts, review the notes
```

The problem number can be left out of `test`, `hint` and `done` while only one problem is in the practice area.

Hints come in five layers, one per call:

| Layer | Shows |
| ----- | ----- |
| 1 | Type: the technique the problem calls for |
| 2 | Recognition signals: what in the statement points to that technique |
| 3 | Steps: brute force, its bottleneck, and how each optimisation removes it |
| 4 | Key idea: the one idea the optimal solution hinges on |
| 5 | The best archived attempt |

The notes themselves are written in Chinese.

Archiving runs the tests again, prints every past attempt's speed on the large input next to this one, asks whether this attempt reached the optimal solution in one go, and prints the notes for review. Every archived redo adds a row to `history.csv` with the date, minutes spent, hint layers used and the optimal answer.

## Commands

| Command | What it does |
| ------- | ------------ |
| `python3 lc.py new "21. Merge Two Sorted Lists"` | Creates the problem folder (notes and test-case templates) and a practice file |
| `python3 lc.py start <problem>` | Starts a problem in the practice area: a first attempt or a blind redo (`redo` is the same command) |
| `python3 lc.py plan [name] [--all]` | Progress through a problem list, by group; lists the problems not done yet |
| `python3 lc.py test [problem]` | Tests practice-area attempts |
| `python3 lc.py hint [problem]` | Reveals the next hint layer |
| `python3 lc.py done [problem] [--optimal yes\|no]` | Archives a passing attempt; the flag skips the question |
| `python3 lc.py list [-d level] [-t type] [--plan name] [--all]` | Unsolved problems grouped by difficulty, then by type (a problem with several types appears under each); `--all` adds solved ones |
| `python3 lc.py next [-n 10] [-d level] [-t type]` | Lists the problems most due for a redo |
| `python3 lc.py check [problem]` | Tests every archived attempt (all problems when none is named) |
| `python3 lc.py index` | Regenerates `REVIEW.md` from the notes |

`<problem>` is a number (`42`) or part of the folder name (`trapping`). A difficulty is `easy`, `medium` or `hard`. A type is matched against each problem's type tags, in English or in the notes' Chinese, ignoring case: a full type name matches only that type (`sorting` does not include topological sort), and anything else matches by substring (`tree` covers both binary tree and binary search tree). `REVIEW.md` lists every type in use.

## Review schedule

In plain terms: a problem comes back for a redo after 3 days; each consecutive redo done with no hints and at the optimal complexity doubles that gap, and any other redo resets it.

`next` ranks problems by days since the last attempt divided by the current gap. A problem that has never been redone counts from the date of its latest archived attempt. Problems never solved are not in `next`; `list` and `plan` show those.

## Layout

| Path | Contents |
| ---- | -------- |
| `problems/<number>_<name>/notes.md` | Study notes: type, recognition signals, steps, key idea, versions (one row per attempt with idea, complexity and verdict) and pitfalls; the header names the best attempt file |
| `problems/<number>_<name>/cases.py` | Sample inputs with expected outputs, plus an optional large input |
| `problems/<number>_<name>/YYmmDD.py` | One file per attempt, named by date; a second attempt on the same day is `YYmmDD_2.py` |
| `problems/<number>_<name>/YYmmDD.java`, `.js` | Earlier Java and JavaScript attempts; kept for reference and not run by the tool |
| `problems/<number>_<name>/template.py` | LeetCode's Python code template; the first attempt's practice file is built from it |
| `plans/<list>.json` | Problem lists (e.g. Top Interview 150) with their groups, in LeetCode's order |
| `problems/booking_<name>/` | Interview problems without a LeetCode number, same layout |
| `practice/` | Attempts in progress; not committed |
| `history.csv` | One row per archived redo |
| `REVIEW.md` | Generated review index grouped by problem type |
| `helpers.py` | `ListNode`, `TreeNode` and converters to and from LeetCode's list notation |
| `algorithms/` | Standalone algorithm practice (heap sort) |
| `lc.py` | The command-line tool |

Each Python attempt is plain LeetCode code: it can be pasted into LeetCode after removing the `helpers` import, if any.

## Test cases

In plain terms: `cases.py` names the method under test and lists inputs with expected outputs; linked lists and trees are built with helpers and compared in LeetCode's list notation.

```python
import random
from helpers import build_linked_list, build_tree

METHOD = "trap"                      # method on Solution
CASES = [
    dict(args=([4, 2, 0, 3, 2, 5],), expected=9),
]

# Optional settings
UNORDERED = True                     # compare lists ignoring order, at every level
CHECK_ARG = 0                        # compare argument 0 after the call (in-place problems)
def check(output, expected, args): ...  # custom comparison: raw return value, arguments after the call
def bench():                         # large input, timed with a 3 s limit
    return ([random.Random(0).randint(0, 10**4) for _ in range(100_000)],)
```

Design problems (a class driven by a sequence of calls) use `CLASS` instead of `METHOD`:

```python
CLASS = "MinStack"
CASES = [
    dict(ops=["MinStack", "push", "getMin"], args=[[], [-2], []], expected=[None, None, -2]),
]
```

Each sample case has a 2-second limit, so an infinite loop shows up as a failed case.

A problem whose only attempts are in Java or JavaScript still has Python test cases, so it can be redone in Python; its first redo starts from a blank class to paste LeetCode's template into.
