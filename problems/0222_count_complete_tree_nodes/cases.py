from helpers import build_tree

METHOD = "countNodes"

CASES = [
    dict(args=(build_tree([1, 2, 3, 4, 5, 6]),), expected=6),
    dict(args=(build_tree([]),), expected=0),
    dict(args=(build_tree([1]),), expected=1),
    dict(args=(build_tree([1, 2]),), expected=2),
    dict(args=(build_tree([1, 2, 3, 4, 5, 6, 7]),), expected=7),
    dict(args=(build_tree([1, 2, 3, 4, 5, 6, 7, 8]),), expected=8),
]


def bench():
    return (build_tree(list(range(1, 50_001))),)
