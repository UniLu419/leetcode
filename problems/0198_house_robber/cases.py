METHOD = "rob"

CASES = [
    dict(args=([1, 2, 3, 1],), expected=4),
    dict(args=([2, 7, 9, 3, 1],), expected=12),
    dict(args=([5],), expected=5),
    dict(args=([2, 1, 1, 2],), expected=4),
    dict(args=([0, 0, 0],), expected=0),
    dict(args=([400] * 100,), expected=20000),
]
