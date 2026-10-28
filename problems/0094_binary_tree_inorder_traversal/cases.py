from helpers import build_tree

METHOD = "inorderTraversal"

CASES = [
    dict(args=(build_tree([1, None, 2, 3]),), expected=[1, 3, 2]),
    dict(args=(build_tree([1, 2, 3, 4, 5, None, 8, None, None, 6, 7, 9]),), expected=[4, 2, 6, 5, 7, 1, 3, 9, 8]),
    dict(args=(build_tree([]),), expected=[]),
    dict(args=(build_tree([1]),), expected=[1]),
    dict(args=(build_tree([3, 2, None, 1]),), expected=[1, 2, 3]),
    dict(args=(build_tree([-1, -1, -1]),), expected=[-1, -1, -1]),
]
