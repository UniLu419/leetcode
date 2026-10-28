METHOD = "buildTree"

CASES = [
    dict(args=([3, 9, 20, 15, 7], [9, 3, 15, 20, 7],), expected=[3, 9, 20, None, None, 15, 7]),
    dict(args=([-1], [-1],), expected=[-1]),
    dict(args=([1, 2, 3], [3, 2, 1]), expected=[1, 2, None, 3]),
    dict(args=([1, 2, 3], [1, 2, 3]), expected=[1, None, 2, None, 3]),
    dict(args=([1, 2, 4, 5, 3, 6], [4, 2, 5, 1, 6, 3]), expected=[1, 2, 3, 4, 5, 6]),
    dict(args=([0, -1, 1], [-1, 0, 1]), expected=[0, -1, 1]),
]
