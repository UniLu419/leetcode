METHOD = "trailingZeroes"

CASES = [
    dict(args=(3,), expected=0),
    dict(args=(5,), expected=1),
    dict(args=(0,), expected=0),
    dict(args=(25,), expected=6),
    dict(args=(30,), expected=7),
    dict(args=(10000,), expected=2499),
]
