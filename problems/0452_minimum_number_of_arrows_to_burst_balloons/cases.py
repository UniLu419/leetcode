import random

METHOD = "findMinArrowShots"

CASES = [
    dict(args=([[10, 16], [2, 8], [1, 6], [7, 12]],), expected=2),
    dict(args=([[1, 2], [3, 4], [5, 6], [7, 8]],), expected=4),
    dict(args=([[1, 2], [2, 3], [3, 4], [4, 5]],), expected=2),
    dict(args=([[1, 2]],), expected=1),
    dict(args=([[1, 10], [2, 3], [4, 5]],), expected=2),
    dict(args=([[1, 2], [1, 2], [1, 2]],), expected=1),
    dict(args=([[-2147483648, 2147483647], [0, 0]],), expected=1),
]


def bench():
    rng = random.Random(0)
    points = []
    for _ in range(100_000):
        a = rng.randint(0, 10**9)
        points.append([a, a + rng.randint(0, 10**4)])
    return (points,)
