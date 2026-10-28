METHOD = "isHappy"

CASES = [
    dict(args=(19,), expected=True),
    dict(args=(2,), expected=False),
    dict(args=(1,), expected=True),
    dict(args=(7,), expected=True),
    dict(args=(4,), expected=False),
    dict(args=(2147483647,), expected=False),
]
