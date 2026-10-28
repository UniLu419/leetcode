import random

from helpers import build_linked_list

METHOD = "sortList"

# An empty result list is None, so its expected value is written as None.
CASES = [
    dict(args=(build_linked_list([4, 2, 1, 3]),), expected=[1, 2, 3, 4]),
    dict(args=(build_linked_list([-1, 5, 3, 4, 0]),), expected=[-1, 0, 3, 4, 5]),
    dict(args=(build_linked_list([]),), expected=None),
    dict(args=(build_linked_list([1]),), expected=[1]),
    dict(args=(build_linked_list([3, 1, 2, 3, 1]),), expected=[1, 1, 2, 3, 3]),
    dict(args=(build_linked_list([5, 4, 3, 2, 1]),), expected=[1, 2, 3, 4, 5]),
    dict(args=(build_linked_list([100000, -100000, 0]),), expected=[-100000, 0, 100000]),
]


def bench():
    rng = random.Random(0)
    return (build_linked_list([rng.randint(-10**5, 10**5) for _ in range(50_000)]),)
