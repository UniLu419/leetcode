import random

METHOD = "insert"

CASES = [
    dict(args=([[1, 3], [6, 9]], [2, 5]), expected=[[1, 5], [6, 9]]),
    dict(args=([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]), expected=[[1, 2], [3, 10], [12, 16]]),
    dict(args=([], [5, 7]), expected=[[5, 7]]),
    dict(args=([[1, 5]], [6, 8]), expected=[[1, 5], [6, 8]]),
    dict(args=([[1, 5]], [0, 0]), expected=[[0, 0], [1, 5]]),
    dict(args=([[3, 5], [12, 15]], [6, 6]), expected=[[3, 5], [6, 6], [12, 15]]),
    dict(args=([[1, 5]], [2, 3]), expected=[[1, 5]]),
    dict(args=([[1, 5]], [0, 6]), expected=[[0, 6]]),
]


def bench():
    return ([[2 * i, 2 * i + 1] for i in range(10_000)], [5_000, 15_000])
