from helpers import build_tree

METHOD = "kthSmallest"

CASES = [
    dict(args=(build_tree([3, 1, 4, None, 2]), 1,), expected=1),
    dict(args=(build_tree([5, 3, 6, 2, 4, None, None, 1]), 3,), expected=3),
    dict(args=(build_tree([1]), 1,), expected=1),
    dict(args=(build_tree([5, 3, 6, 2, 4, None, None, 1]), 6,), expected=6),
    dict(args=(build_tree([3, 2, None, 1]), 3,), expected=3),
    dict(args=(build_tree([2, 1, 3]), 2,), expected=2),
]
