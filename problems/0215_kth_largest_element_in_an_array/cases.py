import random

METHOD = "findKthLargest"

CASES = [
    dict(args=([3, 2, 1, 5, 6, 4], 2,), expected=5),
    dict(args=([3, 2, 3, 1, 2, 4, 5, 5, 6], 4,), expected=4),
    dict(args=([1], 1,), expected=1),
    dict(args=([2, 2, 2], 2,), expected=2),
    dict(args=([-1, -2, -3], 1,), expected=-1),
    dict(args=([10000, -10000, 0], 3,), expected=-10000),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(-5, 5) for _ in range(100_000)], 50_000)
