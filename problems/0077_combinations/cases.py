METHOD = "combine"
UNORDERED = True

CASES = [
    dict(args=(4, 2,), expected=[[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]),
    dict(args=(1, 1,), expected=[[1]]),
    # k == n 只有一种
    dict(args=(3, 3,), expected=[[1, 2, 3]]),
    dict(args=(3, 1,), expected=[[1], [2], [3]]),
    dict(args=(5, 4,), expected=[[1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5]]),
]
