import random

METHOD = "twoSum"

CASES = [
    dict(args=([2, 7, 11, 15], 9), expected=[1, 2]),
    dict(args=([2, 3, 4], 6), expected=[1, 3]),
    dict(args=([-1, 0], -1), expected=[1, 2]),
    dict(args=([0, 0, 3, 4], 0), expected=[1, 2]),
    dict(args=([1, 2, 3, 4, 4, 9, 56, 90], 8), expected=[4, 5]),
    dict(args=([5, 25, 75], 100), expected=[2, 3]),
]


def bench():
    rng = random.Random(0)
    numbers = sorted(rng.randint(-1000, -500) for _ in range(29_998)) + [999, 1000]
    return (numbers, 1999)
