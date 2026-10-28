METHOD = "search"

CASES = [
    dict(args=([4, 5, 6, 7, 0, 1, 2], 0,), expected=4),
    dict(args=([4, 5, 6, 7, 0, 1, 2], 3,), expected=-1),
    dict(args=([1], 0,), expected=-1),
    dict(args=([1], 1,), expected=0),
    dict(args=([3, 1], 1,), expected=1),
    dict(args=([5, 1, 3], 5,), expected=0),
    dict(args=([1, 2, 3, 4, 5], 4,), expected=3),
]
