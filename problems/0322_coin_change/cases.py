import random

METHOD = "coinChange"

CASES = [
    dict(args=([1, 2, 5], 11,), expected=3),
    dict(args=([2], 3,), expected=-1),
    dict(args=([1], 0,), expected=0),
    dict(args=([1, 3, 4], 6), expected=2),
    dict(args=([2147483647], 2), expected=-1),
    dict(args=([186, 419, 83, 408], 6249), expected=20),
]


def bench():
    rng = random.Random(0)
    return (rng.sample(range(1, 500), 12), 10**4)
