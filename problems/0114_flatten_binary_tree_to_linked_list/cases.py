from helpers import build_tree

METHOD = "flatten"
CHECK_ARG = 0

CASES = [
    dict(args=(build_tree([1, 2, 5, 3, 4, None, 6]),), expected=[1, None, 2, None, 3, None, 4, None, 5, None, 6]),
    dict(args=(build_tree([]),), expected=None),
    dict(args=(build_tree([0]),), expected=[0]),
    dict(args=(build_tree([1, 2, None, 3]),), expected=[1, None, 2, None, 3]),
    dict(args=(build_tree([1, None, 2, None, 3]),), expected=[1, None, 2, None, 3]),
    dict(args=(build_tree([-1, -2, -3, -4, -5]),), expected=[-1, None, -2, None, -4, None, -5, None, -3]),
]
