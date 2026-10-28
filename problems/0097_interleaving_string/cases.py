METHOD = "isInterleave"

CASES = [
    dict(args=('aabcc', 'dbbca', 'aadbbcbcac',), expected=True),
    dict(args=('aabcc', 'dbbca', 'aadbbbaccc',), expected=False),
    dict(args=('', '', '',), expected=True),
    dict(args=('', '', 'a',), expected=False),
    dict(args=('a', '', 'a',), expected=True),
    dict(args=('a', 'b', 'abc',), expected=False),
    dict(args=('aa', 'ab', 'aaba',), expected=True),
]
