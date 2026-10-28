METHOD = "reverse"

CASES = [
    dict(args=(123,), expected=321),
    dict(args=(-123,), expected=-321),
    dict(args=(120,), expected=21),
    dict(args=(0,), expected=0),
    dict(args=(1534236469,), expected=0),
    dict(args=(-2147483648,), expected=0),
    dict(args=(1463847412,), expected=2147483641),
]
