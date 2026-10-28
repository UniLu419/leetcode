METHOD = "myPow"

CASES = [
    dict(args=(2.0, 10,), expected=1024.0),
    dict(args=(2.1, 3,), expected=9.261),
    dict(args=(2.0, -2,), expected=0.25),
    dict(args=(-2.0, 3), expected=-8.0),
    dict(args=(0.00001, 2147483647), expected=0.0),
    dict(args=(2.0, -2147483648), expected=0.0),
    dict(args=(-1.0, -2147483647), expected=-1.0),
]
