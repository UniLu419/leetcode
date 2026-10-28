from helpers import build_tree

METHOD = "hasPathSum"

CASES = [
    dict(args=(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]), 22,), expected=True),
    dict(args=(build_tree([1, 2, 3]), 5,), expected=False),
    dict(args=(build_tree([]), 0,), expected=False),
    dict(args=(build_tree([1]), 1), expected=True),
    dict(args=(build_tree([1, 2]), 1), expected=False),
    dict(args=(build_tree([-2, None, -3]), -5), expected=True),
    dict(args=(build_tree([1, -1]), 0), expected=True),
]
