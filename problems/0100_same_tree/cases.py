from helpers import build_tree

METHOD = "isSameTree"

CASES = [
    dict(args=(build_tree([1, 2, 3]), build_tree([1, 2, 3])), expected=True),
    dict(args=(build_tree([1, 2]), build_tree([1, None, 2])), expected=False),
    dict(args=(build_tree([1, 2, 1]), build_tree([1, 1, 2])), expected=False),
    dict(args=(build_tree([]), build_tree([])), expected=True),
    dict(args=(build_tree([1]), build_tree([])), expected=False),
    dict(args=(build_tree([1, None, 2]), build_tree([1, None, 3])), expected=False),
]
