from helpers import build_tree

METHOD = "invertTree"

CASES = [
    dict(args=(build_tree([4, 2, 7, 1, 3, 6, 9]),), expected=[4, 7, 2, 9, 6, 3, 1]),
    dict(args=(build_tree([2, 1, 3]),), expected=[2, 3, 1]),
    dict(args=(build_tree([]),), expected=None),
    dict(args=(build_tree([1]),), expected=[1]),
    dict(args=(build_tree([1, None, 2, None, 3]),), expected=[1, 2, None, 3]),
    dict(args=(build_tree([-1, -2, 3, None, -4]),), expected=[-1, 3, -2, None, None, -4]),
]
