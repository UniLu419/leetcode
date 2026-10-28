from helpers import build_tree

METHOD = "levelOrder"

CASES = [
    dict(args=(build_tree([3, 9, 20, None, None, 15, 7]),), expected=[[3], [9, 20], [15, 7]]),
    dict(args=(build_tree([1]),), expected=[[1]]),
    dict(args=(build_tree([]),), expected=[]),
    dict(args=(build_tree([1, 2, 3, 4, 5, 6, 7]),), expected=[[1], [2, 3], [4, 5, 6, 7]]),
    dict(args=(build_tree([1, 2, None, 3]),), expected=[[1], [2], [3]]),
    dict(args=(build_tree([0, -1, 1, None, -2]),), expected=[[0], [-1, 1], [-2]]),
]
