METHOD = "searchInsert"

CASES = [
    dict(args=([1, 3, 5, 6], 5), expected=2),
    dict(args=([1, 3, 5, 6], 2), expected=1),
    dict(args=([1, 3, 5, 6], 7), expected=4),
    dict(args=([1, 3, 5, 6], 0), expected=0),
    dict(args=([1], 0), expected=0),
    dict(args=([1], 1), expected=0),
    dict(args=([1], 2), expected=1),
    dict(args=([-5, -3, 0, 2, 9], -4), expected=1),
]


def bench():
    return (list(range(0, 20_000, 2)), 12_345)
