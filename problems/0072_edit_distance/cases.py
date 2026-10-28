METHOD = "minDistance"

CASES = [
    dict(args=('horse', 'ros',), expected=3),
    dict(args=('intention', 'execution',), expected=5),
    dict(args=('', '',), expected=0),
    dict(args=('', 'abc',), expected=3),
    dict(args=('abc', 'abc',), expected=0),
    dict(args=('a', 'b',), expected=1),
]
