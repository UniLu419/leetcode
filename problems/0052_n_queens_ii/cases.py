METHOD = "totalNQueens"

CASES = [
    dict(args=(4,), expected=2),
    dict(args=(1,), expected=1),
    # 无解
    dict(args=(2,), expected=0),
    dict(args=(3,), expected=0),
    dict(args=(8,), expected=92),
]


def bench():
    return (9,)
