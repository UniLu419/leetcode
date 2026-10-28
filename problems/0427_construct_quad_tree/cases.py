from collections import deque

METHOD = "construct"


def serialize(root):
    """LeetCode notation: level order of [isLeaf, val], None for a missing child, trailing None trimmed; val of an internal node is written as 1."""
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        leaf = int(bool(node.isLeaf))
        values.append([leaf, int(bool(node.val)) if leaf else 1])
        queue.extend([node.topLeft, node.topRight, node.bottomLeft, node.bottomRight])
    while values and values[-1] is None:
        values.pop()
    return values


def check(output, expected, args):
    """Same tree shape and leaf values as expected; an internal node's val may be either value."""
    return serialize(output) == [v if v is None or v[0] else [0, 1] for v in expected]


CASES = [
    dict(args=([[0, 1], [1, 0]],), expected=[[0, 1], [1, 0], [1, 1], [1, 1], [1, 0]]),
    dict(args=([[1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0], [1, 1, 1, 1, 0, 0, 0, 0]],), expected=[[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]),
    dict(args=([[0]],), expected=[[1, 0]]),
    dict(args=([[1, 1], [1, 1]],), expected=[[1, 1]]),
    dict(args=([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]],), expected=[[1, 0]]),
    dict(args=([[1, 1, 0, 0], [1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0]],), expected=[[0, 1], [1, 1], [1, 0], [1, 1], [0, 1], None, None, None, None, None, None, None, None, None, None, None, None, [1, 1], [1, 1], [1, 1], [1, 0]]),
]
