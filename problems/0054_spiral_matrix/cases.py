METHOD = "spiralOrder"

CASES = [
    dict(args=([[1, 2, 3], [4, 5, 6], [7, 8, 9]],), expected=[1, 2, 3, 6, 9, 8, 7, 4, 5]),
    dict(args=([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],), expected=[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
    dict(args=([[1]],), expected=[1]),
    dict(args=([[1, 2, 3]],), expected=[1, 2, 3]),
    dict(args=([[1], [2], [3]],), expected=[1, 2, 3]),
    dict(args=([[1, 2], [3, 4], [5, 6]],), expected=[1, 2, 4, 6, 5, 3]),
]
