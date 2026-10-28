# LeetCode Practice

In plain terms: every problem lives in its own folder with its test cases, study notes and every past attempt. Redoing a problem happens in a separate practice area that shows only the function signature, so old answers stay out of sight until the new attempt passes and is archived.

Requires Python 3.10+, standard library only.

## Daily loop

In plain terms: pick a problem that is due, solve it blind, reveal hints only when stuck, then archive it and compare with past attempts.

```bash
python3 lc.py next       # problems most due for a redo
python3 lc.py redo 42    # blank practice file: signature only
python3 lc.py test       # sample cases, then a large input for speed
python3 lc.py hint       # reveal the next hint layer
python3 lc.py done       # archive, compare with past attempts, review the notes
```

The problem number can be left out of `test`, `hint` and `done` while only one problem is in the practice area.

Hints come in five layers, one per call:

| Layer | Shows |
| ----- | ----- |
| 1 | 题型 — the problem type |
| 2 | 识别信号 — what in the statement points to that type |
| 3 | 解题步骤 — brute force, its bottleneck, and how each optimisation removes it |
| 4 | 关键一步 — the one idea the optimal solution hinges on |
| 5 | The best archived attempt |

Archiving runs the tests again, prints every past attempt's speed on the large input next to this one, asks whether this attempt reached the optimal solution in one go, and prints the notes for review. Every archived redo adds a row to `history.csv` with the date, minutes spent, hint layers used and the optimal answer.

## Commands

| Command | What it does |
| ------- | ------------ |
| `python3 lc.py new "21. Merge Two Sorted Lists"` | Creates the problem folder (notes and test-case templates) and a practice file |
| `python3 lc.py redo <problem>` | Starts a blind redo of an archived problem |
| `python3 lc.py test [problem]` | Tests practice-area attempts |
| `python3 lc.py hint [problem]` | Reveals the next hint layer |
| `python3 lc.py done [problem] [--optimal yes\|no]` | Archives a passing attempt; the flag skips the question |
| `python3 lc.py next [-n 10]` | Lists the problems most due for a redo |
| `python3 lc.py check [problem]` | Tests every archived attempt (all problems when none is named) |
| `python3 lc.py index` | Regenerates `REVIEW.md` from the notes |

`<problem>` is a number (`42`) or part of the folder name (`trapping`).

## Review schedule

In plain terms: a problem comes back for a redo after 3 days; each consecutive redo done with no hints and at the optimal complexity doubles that gap, and any other redo resets it.

`next` ranks problems by days since the last attempt divided by the current gap. A problem that has never been redone counts from the date of its latest archived attempt.

## Layout

| Path | Contents |
| ---- | -------- |
| `problems/<number>_<name>/notes.md` | Study notes: 题型, 识别信号, 解题步骤, 关键一步, 各版本 (one row per attempt with idea, complexity and verdict), 易错点; the header names the 最优解 file |
| `problems/<number>_<name>/cases.py` | Sample inputs with expected outputs, plus an optional large input |
| `problems/<number>_<name>/YYmmDD.py` | One file per attempt, named by date; a second attempt on the same day is `YYmmDD_2.py` |
| `practice/` | Attempts in progress; not committed |
| `history.csv` | One row per archived redo |
| `REVIEW.md` | Generated review index grouped by problem type |
| `helpers.py` | `ListNode`, `TreeNode` and converters to and from LeetCode's list notation |
| `lc.py` | The command-line tool |

Each attempt file is plain LeetCode code: it can be pasted into LeetCode after removing the `helpers` import, if any.

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
def check(output, expected): ...     # custom comparison
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

## Problems not yet migrated

Python files in the repository root are problems still in the old single-file format. Each one runs on its own and asks for a sample number:

```bash
python3 125_valid_palindrome.py
```

They use `custom_types.py`, `utils.py` and `timing_dec.py`. The Java and JavaScript files are standalone snippets.
