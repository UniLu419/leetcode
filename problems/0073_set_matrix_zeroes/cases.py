import random

METHOD = "setZeroes"
CHECK_ARG = 0

CASES = [
    dict(args=([[1, 1, 1], [1, 0, 1], [1, 1, 1]],), expected=[[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
    dict(
        args=([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]],),
        expected=[[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]],
    ),
    dict(args=([[0]],), expected=[[0]]),
    dict(args=([[1]],), expected=[[1]]),
    dict(args=([[1, 0, 3]],), expected=[[0, 0, 0]]),
    dict(args=([[1, 2], [3, 0], [5, 6]],), expected=[[1, 0], [0, 0], [5, 0]]),
    dict(args=([[0, 0], [0, 0]],), expected=[[0, 0], [0, 0]]),
]


def bench():
    rng = random.Random(0)
    matrix = [[rng.randint(1, 2**31 - 1) for _ in range(200)] for _ in range(200)]
    for _ in range(20):
        matrix[rng.randrange(200)][rng.randrange(200)] = 0
    return (matrix,)
