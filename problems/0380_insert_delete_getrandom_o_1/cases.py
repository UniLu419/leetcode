import random

CLASS = "RandomizedSet"

# getRandom 的期望写成"可接受的值列表"，返回其中任意一个都算对。
CASES = [
    dict(
        ops=["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"],
        args=[[], [1], [2], [2], [], [1], [2], []],
        expected=[None, True, False, True, [1, 2], True, False, [2]],
    ),
    dict(
        ops=["RandomizedSet", "insert", "insert", "remove", "insert", "getRandom"],
        args=[[], [-1], [-2], [-1], [-1], []],
        expected=[None, True, True, True, True, [-1, -2]],
    ),
    dict(
        ops=["RandomizedSet", "insert", "insert", "insert", "remove", "remove", "getRandom", "remove", "remove"],
        args=[[], [1], [2], [3], [1], [3], [], [2], [2]],
        expected=[None, True, True, True, True, True, [2], True, False],
    ),
    dict(
        ops=["RandomizedSet", "insert", "remove", "insert", "getRandom"],
        args=[[], [0], [0], [5], []],
        expected=[None, True, True, True, [5]],
    ),
]


def check(output, expected, args):
    if len(output) != len(expected):
        return False
    for out, exp in zip(output, expected):
        if isinstance(exp, list):
            if out not in exp:
                return False
        elif out != exp:
            return False
    return True


def bench():
    rng = random.Random(0)
    n = 10_000
    vals = rng.sample(range(-(2**31), 2**31 - 1), n)
    ops = ["RandomizedSet"] + ["insert"] * n + ["getRandom"] * n
    args = [[]] + [[v] for v in vals] + [[] for _ in range(n)]
    return (ops, args)
