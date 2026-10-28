METHOD = "isPalindrome"

CASES = [
    dict(args=(121,), expected=True),
    dict(args=(-121,), expected=False),
    dict(args=(10,), expected=False),
    dict(args=(0,), expected=True),
    dict(args=(7,), expected=True),
    dict(args=(1221,), expected=True),
    dict(args=(1000021,), expected=False),
]
