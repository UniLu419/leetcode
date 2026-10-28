from helpers import build_tree

METHOD = "sumNumbers"

CASES = [
    dict(args=(build_tree([1, 2, 3]),), expected=25),
    dict(args=(build_tree([4, 9, 0, 5, 1]),), expected=1026),
    dict(args=(build_tree([0]),), expected=0),
    dict(args=(build_tree([2, 0, 3, None, 5]),), expected=228),
    dict(args=(build_tree([1, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0]),), expected=1000000000),
]
