METHOD = "searchRange"

CASES = [
    dict(args=([5, 7, 7, 8, 8, 10], 8,), expected=[3, 4]),
    dict(args=([5, 7, 7, 8, 8, 10], 6,), expected=[-1, -1]),
    dict(args=([], 0,), expected=[-1, -1]),
    dict(args=([1], 1,), expected=[0, 0]),
    dict(args=([2, 2, 2, 2], 2,), expected=[0, 3]),
    dict(args=([1, 3], 4,), expected=[-1, -1]),
    dict(args=([-1000000000, 0, 0, 1000000000], 1000000000,), expected=[3, 3]),
]


def bench():
    return ([-1] + [7] * 99_998 + [9], 7)
