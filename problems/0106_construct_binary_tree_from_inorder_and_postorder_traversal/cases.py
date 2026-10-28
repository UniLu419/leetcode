METHOD = "buildTree"

CASES = [
    dict(args=([9, 3, 15, 20, 7], [9, 15, 7, 20, 3],), expected=[3, 9, 20, None, None, 15, 7]),
    dict(args=([-1], [-1],), expected=[-1]),
    dict(args=([3, 2, 1], [3, 2, 1]), expected=[1, 2, None, 3]),
    dict(args=([1, 2, 3], [3, 2, 1]), expected=[1, None, 2, None, 3]),
    dict(args=([4, 2, 5, 1, 6, 3], [4, 5, 2, 6, 3, 1]), expected=[1, 2, 3, 4, 5, 6]),
    dict(args=([-1, 0, 1], [-1, 1, 0]), expected=[0, -1, 1]),
]
