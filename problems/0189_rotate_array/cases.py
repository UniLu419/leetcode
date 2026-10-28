import random

METHOD = "rotate"
CHECK_ARG = 0

CASES = [
    dict(args=([1, 2, 3, 4, 5, 6, 7], 3), expected=[5, 6, 7, 1, 2, 3, 4]),
    dict(args=([-1, -100, 3, 99], 2), expected=[3, 99, -1, -100]),
    dict(args=([1], 0), expected=[1]),
    dict(args=([1, 2], 3), expected=[2, 1]),
    dict(args=([1, 2, 3], 3), expected=[1, 2, 3]),
    dict(args=([1, 2, 3, 4], 0), expected=[1, 2, 3, 4]),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(-(2**31), 2**31 - 1) for _ in range(100_000)], 50_000)
