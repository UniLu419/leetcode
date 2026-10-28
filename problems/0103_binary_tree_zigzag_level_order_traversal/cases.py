from helpers import build_tree

METHOD = "zigzagLevelOrder"

CASES = [
    dict(args=(build_tree([3, 9, 20, None, None, 15, 7]),), expected=[[3], [20, 9], [15, 7]]),
    dict(args=(build_tree([1]),), expected=[[1]]),
    dict(args=(build_tree([]),), expected=[]),
    dict(args=(build_tree([1, 2, 3, 4, 5, 6, 7]),), expected=[[1], [3, 2], [4, 5, 6, 7]]),
    dict(args=(build_tree(list(range(1, 16))),), expected=[[1], [3, 2], [4, 5, 6, 7], [15, 14, 13, 12, 11, 10, 9, 8]]),
    dict(args=(build_tree([1, 2, None, 3, None, 4]),), expected=[[1], [2], [3], [4]]),
]
