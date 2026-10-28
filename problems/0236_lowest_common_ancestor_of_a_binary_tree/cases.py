from helpers import build_tree

METHOD = "lowestCommonAncestor"


def nodes_of(root):
    stack, nodes = [root] if root else [], []
    while stack:
        node = stack.pop()
        nodes.append(node)
        stack += [c for c in (node.left, node.right) if c is not None]
    return nodes


def case(values, p, q):
    """Builds the tree and passes p and q as the tree's own nodes with those values."""
    root = build_tree(values)
    by_val = {n.val: n for n in nodes_of(root)}
    return (root, by_val[p], by_val[q])


def check(output, expected, args):
    """The answer must be the tree's own node (not a copy) holding the expected value."""
    return any(n is output for n in nodes_of(args[0])) and output.val == expected


CASES = [
    dict(args=case([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1), expected=3),
    dict(args=case([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4), expected=5),
    dict(args=case([1, 2], 1, 2), expected=1),
    dict(args=case([-1, 0, 3, -2, 4, None, None, 8], 8, 4), expected=0),
    dict(args=case([-1, 0, 3, -2, 4, None, None, 8], 8, 3), expected=-1),
    dict(args=case([1, 2, None, 3, None, 4], 4, 2), expected=2),
]
