from collections import deque

METHOD = "connect"


class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def build(values):
    """LeetCode level-order notation -> Node tree with every next pointer None."""
    if not values or values[0] is None:
        return None
    root = Node(values[0])
    queue, i = deque([root]), 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = Node(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root


def check(output, expected, args):
    """Each level, walked by next from its leftmost node, must be exactly that level; serialized as LeetCode's "#"-separated levels."""
    if output is not args[0]:
        return False
    serialized, level = [], [output] if output is not None else []
    while level:
        walk, node = [], level[0]
        while node is not None and len(walk) <= len(level):
            walk.append(node)
            node = node.next
        if [id(n) for n in walk] != [id(n) for n in level]:
            return False
        serialized += [n.val for n in level] + ["#"]
        level = [c for n in level for c in (n.left, n.right) if c is not None]
    return serialized == expected


CASES = [
    dict(args=(build([1, 2, 3, 4, 5, None, 7]),), expected=[1, "#", 2, 3, "#", 4, 5, 7, "#"]),
    dict(args=(build([]),), expected=[]),
    dict(args=(build([1]),), expected=[1, "#"]),
    dict(args=(build([1, 2, 3, 4, None, None, 5]),), expected=[1, "#", 2, 3, "#", 4, 5, "#"]),
    dict(args=(build([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]),), expected=[1, "#", 2, 3, "#", 4, 5, 6, "#", 7, 8, "#"]),
    dict(args=(build([0, -100, 100]),), expected=[0, "#", -100, 100, "#"]),
]
