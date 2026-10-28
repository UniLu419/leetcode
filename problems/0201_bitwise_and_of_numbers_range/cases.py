METHOD = "rangeBitwiseAnd"

CASES = [
    dict(args=(5, 7,), expected=4),
    dict(args=(0, 0,), expected=0),
    dict(args=(1, 2147483647,), expected=0),
    dict(args=(1, 1), expected=1),
    dict(args=(6, 7), expected=6),
    dict(args=(2147483646, 2147483647), expected=2147483646),
]


def bench():
    # The result 2^30 is never 0, so a loop over the range cannot stop early.
    return (1073741824, 2147483647)
