from helpers import build_tree

METHOD = "isValidBST"

CASES = [
    dict(args=(build_tree([2, 1, 3]),), expected=True),
    dict(args=(build_tree([5, 1, 4, None, None, 3, 6]),), expected=False),
    dict(args=(build_tree([5, 4, 6, None, None, 3, 7]),), expected=False),
    dict(args=(build_tree([2, 2, 2]),), expected=False),
    dict(args=(build_tree([2147483647]),), expected=True),
    dict(args=(build_tree([-2147483648, None, 2147483647]),), expected=True),
]
