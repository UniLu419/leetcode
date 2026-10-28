import random

METHOD = "maxSubArray"

CASES = [
    dict(args=([-2, 1, -3, 4, -1, 2, 1, -5, 4],), expected=6),
    dict(args=([1],), expected=1),
    dict(args=([5, 4, -1, 7, 8],), expected=23),
    dict(args=([-1],), expected=-1),
    dict(args=([-3, -1, -2],), expected=-1),
    dict(args=([2, -1, 2],), expected=3),
    dict(args=([10000, -10000, 10000],), expected=10000),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(-10**4, 10**4) for _ in range(100_000)],)
