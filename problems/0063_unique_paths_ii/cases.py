METHOD = "uniquePathsWithObstacles"

CASES = [
    dict(args=([[0, 0, 0], [0, 1, 0], [0, 0, 0]],), expected=2),
    dict(args=([[0, 1], [0, 0]],), expected=1),
    dict(args=([[0]],), expected=1),
    dict(args=([[1]],), expected=0),
    dict(args=([[0, 0], [0, 1]],), expected=0),
    dict(args=([[0, 1, 0, 0]],), expected=0),
    dict(args=([[0, 0, 0, 0], [0, 1, 0, 0], [0, 0, 0, 0]],), expected=4),
]
