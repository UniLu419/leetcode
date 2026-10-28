METHOD = "copyRandomList"


class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


def build(pairs):
    """LeetCode notation [[val, random_index], ...] -> head."""
    nodes = [Node(val) for val, _ in pairs]
    for i, (_, r) in enumerate(pairs):
        if i + 1 < len(nodes):
            nodes[i].next = nodes[i + 1]
        nodes[i].random = nodes[r] if r is not None else None
    return nodes[0] if nodes else None


def nodes_of(head):
    nodes = []
    while head is not None:
        nodes.append(head)
        head = head.next
    return nodes


def serialize(head):
    nodes = nodes_of(head)
    index = {id(n): i for i, n in enumerate(nodes)}
    return [[n.val, index[id(n.random)] if n.random is not None else None] for n in nodes]


def check(output, expected, args):
    """Copy must match the expected structure, share no node with the original, and leave the original intact."""
    original = {id(n) for n in nodes_of(args[0])}
    copied = nodes_of(output)
    if any(id(n) in original or (n.random is not None and id(n.random) in original) for n in copied):
        return False
    return serialize(output) == expected and serialize(args[0]) == expected


CASES = [
    dict(args=(build([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),), expected=[[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
    dict(args=(build([[1, 1], [2, 1]]),), expected=[[1, 1], [2, 1]]),
    dict(args=(build([[3, None], [3, 0], [3, None]]),), expected=[[3, None], [3, 0], [3, None]]),
    dict(args=(build([]),), expected=[]),
    dict(args=(build([[-5, 0]]),), expected=[[-5, 0]]),
]
