METHOD = "searchMatrix"

CASES = [
    dict(args=([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3,), expected=True),
    dict(args=([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13,), expected=False),
    dict(args=([[1]], 1,), expected=True),
    dict(args=([[1], [3]], 3,), expected=True),
    dict(args=([[1, 3]], 2,), expected=False),
    dict(args=([[-10000, -5], [7, 10000]], 10001,), expected=False),
]


def bench():
    values = list(range(-10000, 10000, 2))
    return ([values[i:i + 100] for i in range(0, 10000, 100)], 9999)
