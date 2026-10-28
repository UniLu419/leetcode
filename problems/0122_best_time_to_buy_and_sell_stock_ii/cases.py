import random

METHOD = "maxProfit"

CASES = [
    dict(args=([7, 1, 5, 3, 6, 4],), expected=7),
    dict(args=([1, 2, 3, 4, 5],), expected=4),
    dict(args=([7, 6, 4, 3, 1],), expected=0),
    dict(args=([1],), expected=0),
    dict(args=([2, 2, 5],), expected=3),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(0, 10**4) for _ in range(30_000)],)
