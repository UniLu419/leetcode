import random

METHOD = "productExceptSelf"

CASES = [
    dict(args=([1, 2, 3, 4],), expected=[24, 12, 8, 6]),
    dict(args=([-1, 1, 0, -3, 3],), expected=[0, 0, 9, 0, 0]),
    dict(args=([2, 3],), expected=[3, 2]),
    dict(args=([0, 0],), expected=[0, 0]),
    dict(args=([0, 4, 0],), expected=[0, 0, 0]),
    dict(args=([5, 0, 2],), expected=[0, 10, 0]),
]


def bench():
    rng = random.Random(0)
    return ([rng.choice([1, -1]) for _ in range(100_000)],)
