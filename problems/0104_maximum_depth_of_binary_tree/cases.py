import random

from helpers import build_tree

METHOD = "maxDepth"

CASES = [
    dict(args=(build_tree([3, 9, 20, None, None, 15, 7]),), expected=3),
    dict(args=(build_tree([1, None, 2]),), expected=2),
    dict(args=(build_tree([]),), expected=0),
    dict(args=(build_tree([0]),), expected=1),
    dict(args=(build_tree([1, 2, None, 3, None, 4]),), expected=4),
]


def bench():
    rng = random.Random(0)
    return (build_tree([rng.randint(-100, 100) for _ in range(10_000)]),)
