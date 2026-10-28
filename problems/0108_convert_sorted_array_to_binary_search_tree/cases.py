import random

METHOD = "sortedArrayToBST"


def check(output, expected, args):
    """Any height-balanced BST is accepted: its inorder must equal nums and every node must be balanced."""
    values, stack, node = [], [], output
    while stack or node:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        values.append(node.val)
        node = node.right

    def height(node):
        if node is None:
            return 0
        left, right = height(node.left), height(node.right)
        if left < 0 or right < 0 or abs(left - right) > 1:
            return -1
        return max(left, right) + 1

    return values == args[0] and height(output) >= 0


CASES = [
    dict(args=([-10, -3, 0, 5, 9],), expected=[0, -3, 9, -10, None, 5]),
    dict(args=([1, 3],), expected=[3, 1]),
    dict(args=([0],), expected=[0]),
    dict(args=([1, 2, 3, 4],), expected=[2, 1, 3, None, None, None, 4]),
    dict(args=([1, 2, 3, 4, 5, 6, 7],), expected=[4, 2, 6, 1, 3, 5, 7]),
]


def bench():
    return (sorted(random.Random(0).sample(range(-(10**4), 10**4), 10_000)),)
