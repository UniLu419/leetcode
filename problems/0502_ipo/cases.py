import random

METHOD = "findMaximizedCapital"

CASES = [
    dict(args=(2, 0, [1, 2, 3], [0, 1, 1],), expected=4),
    dict(args=(3, 0, [1, 2, 3], [0, 1, 2],), expected=6),
    dict(args=(1, 0, [1], [1],), expected=0),
    dict(args=(10, 0, [1, 2, 3], [0, 1, 2],), expected=6),
    dict(args=(3, 0, [5, 1, 2], [0, 0, 6],), expected=8),
    dict(args=(1, 1000000000, [10000], [1000000000],), expected=1000010000),
]


def bench():
    rng = random.Random(0)
    n = 100_000
    return (n, 1000, [rng.randint(0, 10**4) for _ in range(n)], [rng.randint(0, 10**6) for _ in range(n)])
