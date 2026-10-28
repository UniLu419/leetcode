import random

METHOD = "highestRankedKItems"

CASES = [
    dict(args=([[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]], [2, 5], [0, 0], 3), expected=[[0, 1], [1, 1], [2, 1]]),
    dict(args=([[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]], [2, 3], [2, 3], 2), expected=[[2, 1], [1, 2]]),
    dict(args=([[1, 1, 1], [0, 0, 1], [2, 3, 4]], [2, 3], [0, 0], 3), expected=[[2, 1], [2, 0]]),
    dict(args=([[0, 2, 0]], [2, 2], [0, 1], 1), expected=[[0, 1]]),
    dict(args=([[1, 2], [2, 1]], [2, 2], [0, 0], 2), expected=[[0, 1], [1, 0]]),
    dict(args=([[1, 0, 3]], [2, 5], [0, 0], 1), expected=[]),
    dict(args=([[1, 5, 2]], [2, 5], [0, 0], 2), expected=[[0, 1], [0, 2]]),
]


def bench():
    rng = random.Random(0)
    grid = [[0 if rng.random() < 0.1 else rng.randint(1, 10**5) for _ in range(300)] for _ in range(300)]
    grid[0][0] = 1
    return (grid, [2, 10**5], [0, 0], 300 * 300)
