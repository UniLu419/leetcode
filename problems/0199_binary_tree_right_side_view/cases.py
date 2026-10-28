from helpers import build_tree

METHOD = "rightSideView"

CASES = [
    dict(args=(build_tree([1, 2, 3, None, 5, None, 4]),), expected=[1, 3, 4]),
    dict(args=(build_tree([1, 2, 3, 4, None, None, None, 5]),), expected=[1, 3, 4, 5]),
    dict(args=(build_tree([1, None, 3]),), expected=[1, 3]),
    dict(args=(build_tree([]),), expected=[]),
    dict(args=(build_tree([7]),), expected=[7]),
    dict(args=(build_tree([1, 2, None, 3]),), expected=[1, 2, 3]),
    dict(args=(build_tree([-1, -2, -3, None, -4]),), expected=[-1, -3, -4]),
]
