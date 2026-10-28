METHOD = "lengthOfLIS"

CASES = [
    dict(args=([10, 9, 2, 5, 3, 7, 101, 18],), expected=4),
    dict(args=([0, 1, 0, 3, 2, 3],), expected=4),
    dict(args=([7, 7, 7, 7, 7, 7, 7],), expected=1),
    dict(args=([5],), expected=1),
    dict(args=([-2, -1],), expected=2),
    dict(args=([4, 10, 4, 3, 8, 9],), expected=3),
    dict(args=([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12],), expected=6),
]
