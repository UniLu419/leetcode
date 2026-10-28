from helpers import build_tree

METHOD = "averageOfLevels"

CASES = [
    dict(args=(build_tree([3, 9, 20, None, None, 15, 7]),), expected=[3.0, 14.5, 11.0]),
    dict(args=(build_tree([3, 9, 20, 15, 7]),), expected=[3.0, 14.5, 11.0]),
    dict(args=(build_tree([1]),), expected=[1.0]),
    dict(args=(build_tree([-1, -2, 3]),), expected=[-1.0, 0.5]),
    dict(args=(build_tree([2147483647, 2147483647, 2147483647]),), expected=[2147483647.0, 2147483647.0]),
    dict(args=(build_tree([-2147483648, -2147483648, 2147483647]),), expected=[-2147483648.0, -0.5]),
]
