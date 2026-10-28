import random

from helpers import TreeNode, build_tree

METHOD = "maxPathSum"

CASES = [
    dict(args=(build_tree([1, 2, 3]),), expected=6),
    dict(args=(build_tree([-10, 9, 20, None, None, 15, 7]),), expected=42),
    dict(args=(build_tree([-3]),), expected=-3),
    dict(args=(build_tree([-2, -1]),), expected=-1),
    dict(args=(build_tree([-10, 5, 6]),), expected=6),
    dict(args=(build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1]),), expected=48),
]


def bench():
    """30 000 nodes: a 63-node complete top with a 467-node random chain under each of its 64 child slots."""
    rng = random.Random(0)
    value = lambda: rng.randint(-1000, 1000)
    root = TreeNode(value())
    level = [root]
    for _ in range(5):
        nxt = []
        for node in level:
            node.left, node.right = TreeNode(value()), TreeNode(value())
            nxt += [node.left, node.right]
        level = nxt
    for leaf in level:
        for side in ("left", "right"):
            node = TreeNode(value())
            setattr(leaf, side, node)
            for _ in range(466):
                child = TreeNode(value())
                setattr(node, rng.choice(("left", "right")), child)
                node = child
    return (root,)
