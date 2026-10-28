import random

METHOD = "maxSubarraySumCircular"

CASES = [
    dict(args=([1, -2, 3, -2],), expected=3),
    dict(args=([5, -3, 5],), expected=10),
    dict(args=([-3, -2, -3],), expected=-2),
    dict(args=([5],), expected=5),
    dict(args=([8, -1, -3, 8],), expected=16),
    dict(args=([3, -1, 2, -1],), expected=4),
    dict(args=([-30000, -30000],), expected=-30000),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(-3 * 10**4, 3 * 10**4) for _ in range(30_000)],)
