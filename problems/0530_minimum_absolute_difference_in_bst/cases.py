import random

from helpers import TreeNode, build_tree

METHOD = "getMinimumDifference"


def balanced_bst(values):
    """Height-balanced BST from sorted distinct values."""
    if not values:
        return None
    mid = len(values) // 2
    return TreeNode(values[mid], balanced_bst(values[:mid]), balanced_bst(values[mid + 1:]))


CASES = [
    dict(args=(build_tree([4, 2, 6, 1, 3]),), expected=1),
    dict(args=(build_tree([1, 0, 48, None, None, 12, 49]),), expected=1),
    dict(args=(build_tree([1, None, 3]),), expected=2),
    dict(args=(build_tree([0, None, 100000]),), expected=100000),
    dict(args=(build_tree([236, 104, 701, None, 227, None, 911]),), expected=9),
]


def bench():
    rng = random.Random(0)
    return (balanced_bst(sorted(rng.sample(range(100001), 10000))),)
