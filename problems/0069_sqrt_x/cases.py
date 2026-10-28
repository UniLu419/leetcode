METHOD = "mySqrt"

CASES = [
    dict(args=(4,), expected=2),
    dict(args=(8,), expected=2),
    dict(args=(0,), expected=0),
    dict(args=(1,), expected=1),
    dict(args=(2147395599,), expected=46339),
    dict(args=(2147395600,), expected=46340),
    dict(args=(2147483647,), expected=46340),
]
