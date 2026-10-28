import random

METHOD = "maxProfit"

CASES = [
    dict(args=([7, 1, 5, 3, 6, 4],), expected=5),
    dict(args=([7, 6, 4, 3, 1],), expected=0),
    dict(args=([1],), expected=0),
    dict(args=([2, 4, 1],), expected=2),
    dict(args=([3, 3, 3],), expected=0),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(0, 10**4) for _ in range(100_000)],)
