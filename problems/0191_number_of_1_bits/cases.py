METHOD = "hammingWeight"

CASES = [
    dict(args=(11,), expected=3),
    dict(args=(128,), expected=1),
    dict(args=(2147483645,), expected=30),
    dict(args=(1,), expected=1),
    dict(args=(2147483647,), expected=31),
    dict(args=(1073741824,), expected=1),
]
