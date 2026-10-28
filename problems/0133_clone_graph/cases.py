from collections import deque

METHOD = "cloneGraph"
# 解答文件里 Node 类只在模板注释中，需要自己取消注释（或用 type(node)(...) 构造克隆节点）。


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def build(adj):
    """LeetCode adjacency list (node i + 1 is adj[i]) -> node 1, or None for an empty graph."""
    nodes = [Node(i + 1) for i in range(len(adj))]
    for node, neighbors in zip(nodes, adj):
        node.neighbors = [nodes[v - 1] for v in neighbors]
    return nodes[0] if nodes else None


def reachable(start):
    seen = {id(start): start}
    queue = deque([start])
    while queue:
        for nb in queue.popleft().neighbors:
            if id(nb) not in seen:
                seen[id(nb)] = nb
                queue.append(nb)
    return list(seen.values())


def adjacency(start):
    """Adjacency list by value; None when two distinct nodes share a value or values are not 1..n."""
    nodes = reachable(start)
    by_val = {n.val: n for n in nodes}
    if len(by_val) != len(nodes) or set(by_val) != set(range(1, len(nodes) + 1)):
        return None
    return [[nb.val for nb in by_val[v].neighbors] for v in range(1, len(nodes) + 1)]


def check(output, expected, args):
    """Clone must have the expected adjacency, start at the same value, share no node with the original, and leave it intact."""
    original = args[0]
    if original is None:
        return output is None
    if output is None or output.val != original.val:
        return False
    original_ids = {id(n) for n in reachable(original)}
    if any(id(n) in original_ids for n in reachable(output)):
        return False
    return adjacency(output) == expected and adjacency(original) == expected


CASES = [
    dict(args=(build([[2, 4], [1, 3], [2, 4], [1, 3]]),), expected=[[2, 4], [1, 3], [2, 4], [1, 3]]),
    dict(args=(build([[]]),), expected=[[]]),
    dict(args=(build([]),), expected=[]),
    dict(args=(build([[2], [1]]),), expected=[[2], [1]]),
    dict(args=(build([[2, 3], [1, 3], [1, 2]]),), expected=[[2, 3], [1, 3], [1, 2]]),
    dict(args=(build([[2, 3, 4, 5], [1], [1], [1], [1]]),), expected=[[2, 3, 4, 5], [1], [1], [1], [1]]),
]
