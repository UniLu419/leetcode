METHOD = "reverseBits"

CASES = [
    dict(args=(43261596,), expected=964176192),
    dict(args=(2147483644,), expected=1073741822),
    dict(args=(0,), expected=0),
    dict(args=(2,), expected=1073741824),
    dict(args=(1073741824,), expected=2),
    dict(args=(2147483646,), expected=2147483646),
]
