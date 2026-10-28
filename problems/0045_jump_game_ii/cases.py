import random

METHOD = "jump"

CASES = [
    dict(args=([2, 3, 1, 1, 4],), expected=2),
    dict(args=([2, 3, 0, 1, 4],), expected=2),
    dict(args=([0],), expected=0),
    dict(args=([1, 2],), expected=1),
    dict(args=([1, 1, 1, 1],), expected=3),
    dict(args=([10, 1, 1],), expected=1),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(1, 1000) for _ in range(10_000)],)
