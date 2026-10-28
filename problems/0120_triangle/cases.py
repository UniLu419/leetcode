METHOD = "minimumTotal"

CASES = [
    dict(args=([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]],), expected=11),
    dict(args=([[-10]],), expected=-10),
    dict(args=([[1], [2, 3]],), expected=3),
    dict(args=([[-1], [2, 3], [1, -1, -3]],), expected=-1),
    dict(args=([[1], [2, 3], [100, 100, 1]],), expected=5),
]
