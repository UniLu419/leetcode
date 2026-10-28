METHOD = "hIndex"

CASES = [
    dict(args=([3, 0, 6, 1, 5],), expected=3),
    dict(args=([1, 3, 1],), expected=1),
    dict(args=([0],), expected=0),
    dict(args=([100],), expected=1),
    dict(args=([0, 0, 0],), expected=0),
    dict(args=([4, 4, 4, 4],), expected=4),
]
