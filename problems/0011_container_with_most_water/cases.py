import random

METHOD = "maxArea"

CASES = [
    dict(args=([1, 8, 6, 2, 5, 4, 8, 3, 7],), expected=49),
    dict(args=([1, 1],), expected=1),
    dict(args=([4, 3, 2, 1, 4],), expected=16),
    dict(args=([1, 2, 1],), expected=2),
    dict(args=([2, 2, 2, 2],), expected=6),
    dict(args=([0, 0],), expected=0),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(0, 10**4) for _ in range(100_000)],)
