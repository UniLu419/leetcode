from helpers import build_tree

METHOD = "isSymmetric"

CASES = [
    dict(args=(build_tree([1, 2, 2, 3, 4, 4, 3]),), expected=True),
    dict(args=(build_tree([1, 2, 2, None, 3, None, 3]),), expected=False),
    dict(args=(build_tree([1]),), expected=True),
    dict(args=(build_tree([1, 2, 2, 2, None, 2]),), expected=False),
    dict(args=(build_tree([1, 2, 3]),), expected=False),
    dict(args=(build_tree([1, 2, 2, None, 3, 3]),), expected=True),
]
