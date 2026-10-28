import random

METHOD = "maxProfit"

CASES = [
    dict(args=([3, 3, 5, 0, 0, 3, 1, 4],), expected=6),
    dict(args=([1, 2, 3, 4, 5],), expected=4),
    dict(args=([7, 6, 4, 3, 1],), expected=0),
    dict(args=([1],), expected=0),
    dict(args=([1, 2],), expected=1),
    dict(args=([2, 1, 2, 0, 1],), expected=2),
    dict(args=([1, 2, 4, 2, 5, 7, 2, 4, 9, 0],), expected=13),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(0, 10**5) for _ in range(10**4)],)
