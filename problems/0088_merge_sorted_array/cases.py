METHOD = "merge"
CHECK_ARG = 0

CASES = [
    dict(args=([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3), expected=[1, 2, 2, 3, 5, 6]),
    dict(args=([1], 1, [], 0), expected=[1]),
    dict(args=([0], 0, [1], 1), expected=[1]),
    dict(args=([2, 0], 1, [1], 1), expected=[1, 2]),
    dict(args=([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3), expected=[1, 2, 3, 4, 5, 6]),
    dict(args=([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3), expected=[-1, 0, 0, 1, 2, 2, 3, 3, 3]),
]
