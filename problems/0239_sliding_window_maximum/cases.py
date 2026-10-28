import random

METHOD = "maxSlidingWindow"

CASES = [
    dict(args=([1, 3, -1, -3, 5, 3, 6, 7], 3), expected=[3, 3, 5, 5, 6, 7]),
    dict(args=([1], 1), expected=[1]),
    dict(args=([1, -1], 1), expected=[1, -1]),
    dict(args=([9, 11], 2), expected=[11]),
    dict(args=([7, 2, 4], 2), expected=[7, 4]),
    dict(args=([1, 3, 1, 2, 0, 5], 3), expected=[3, 3, 2, 5]),
    dict(args=([2, 2, 2, 2], 2), expected=[2, 2, 2]),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(-10**4, 10**4) for _ in range(100_000)], 50_000)
