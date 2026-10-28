import random


METHOD = "minSubArrayLen"

CASES = [
    dict(args=(7, [2, 3, 1, 2, 4, 3]), expected=2),
    dict(args=(4, [1, 4, 4]), expected=1),
    dict(args=(11, [1, 1, 1, 1, 1, 1, 1, 1]), expected=0),
    dict(args=(11, [1, 2, 3, 4, 5]), expected=3),
    dict(args=(15, [1, 2, 3, 4, 5]), expected=5),
    dict(args=(1, [1]), expected=1),
    dict(args=(100, [1]), expected=0),
]


def bench():
    rng = random.Random(0)
    return (10**6, [rng.randint(1, 10**4) for _ in range(100_000)])
