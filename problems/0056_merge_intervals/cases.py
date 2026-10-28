import random

METHOD = "merge"

CASES = [
    dict(args=([[1, 3], [2, 6], [8, 10], [15, 18]],), expected=[[1, 6], [8, 10], [15, 18]]),
    dict(args=([[1, 4], [4, 5]],), expected=[[1, 5]]),
    dict(args=([[4, 7], [1, 4]],), expected=[[1, 7]]),
    dict(args=([[1, 4]],), expected=[[1, 4]]),
    dict(args=([[1, 4], [2, 3]],), expected=[[1, 4]]),
    dict(args=([[1, 4], [0, 0]],), expected=[[0, 0], [1, 4]]),
    dict(args=([[1, 2], [1, 5], [1, 3]],), expected=[[1, 5]]),
]


def bench():
    rng = random.Random(0)
    intervals = []
    for _ in range(10_000):
        start = rng.randint(0, 10**4)
        intervals.append([start, start + rng.randint(0, 3)])
    return (intervals,)
