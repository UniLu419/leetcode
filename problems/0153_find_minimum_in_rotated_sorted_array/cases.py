METHOD = "findMin"

CASES = [
    dict(args=([3, 4, 5, 1, 2],), expected=1),
    dict(args=([4, 5, 6, 7, 0, 1, 2],), expected=0),
    dict(args=([11, 13, 15, 17],), expected=11),
    dict(args=([1],), expected=1),
    dict(args=([2, 1],), expected=1),
    dict(args=([2, 3, 4, 5, 1],), expected=1),
    dict(args=([5000, -5000],), expected=-5000),
]
