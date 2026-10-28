from helpers import build_tree

METHOD = "isBalanced"

CASES = [
    dict(args=(build_tree([3, 9, 20, None, None, 15, 7]),), expected=True),
    dict(args=(build_tree([1, 2, 2, 3, 3, None, None, 4, 4]),), expected=False),
    dict(args=(build_tree([]),), expected=True),
    dict(args=(build_tree([1, 2, 2, 3, None, None, 3, 4, None, None, 4]),), expected=False),
    dict(args=(build_tree([1, None, 2, None, 3]),), expected=False),
    dict(args=(build_tree([1, 2]),), expected=True),
]
