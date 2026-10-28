import random

METHOD = "maxPoints"

CASES = [
    dict(args=([[1, 1], [2, 2], [3, 3]],), expected=3),
    dict(args=([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]],), expected=4),
    dict(args=([[0, 0]],), expected=1),
    dict(args=([[0, 0], [0, 1], [0, 2], [1, 5]],), expected=3),
    dict(args=([[0, 0], [1, -1], [2, -2], [3, 3], [-1, 1]],), expected=4),
    dict(args=([[-10000, -10000], [10000, 10000], [0, 1], [1, 0]],), expected=2),
]


def bench():
    rng = random.Random(0)
    points = set()
    while len(points) < 300:
        points.add((rng.randint(-10**4, 10**4), rng.randint(-10**4, 10**4)))
    return ([list(p) for p in sorted(points)],)
