import random

METHOD = "trap"

CASES = [
    dict(args=([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],), expected=6),
    dict(args=([4, 2, 0, 3, 2, 5],), expected=9),
    dict(args=([1],), expected=0),
    dict(args=([2, 0, 2],), expected=2),
    dict(args=([5, 4, 1, 2],), expected=1),
    dict(args=([1, 2, 3, 4],), expected=0),
    dict(args=([3, 0, 0, 0, 3],), expected=9),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(0, 10**4) for _ in range(100_000)],)
