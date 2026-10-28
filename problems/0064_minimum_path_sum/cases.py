METHOD = "minPathSum"

CASES = [
    dict(args=([[1, 3, 1], [1, 5, 1], [4, 2, 1]],), expected=7),
    dict(args=([[1, 2, 3], [4, 5, 6]],), expected=12),
    dict(args=([[5]],), expected=5),
    dict(args=([[1, 2, 3]],), expected=6),
    dict(args=([[1], [2], [3]],), expected=6),
    dict(args=([[0, 0], [0, 0]],), expected=0),
]
