"""LeetCode node types and converters between them and LeetCode's list notation."""

from collections import deque
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_linked_list(values: List) -> Optional[ListNode]:
    """[1, 2, 3] -> 1 -> 2 -> 3"""
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def linked_list_to_list(head: Optional[ListNode]) -> List:
    values = []
    while head is not None:
        values.append(head.val)
        head = head.next
    return values


def build_tree(values: List) -> Optional[TreeNode]:
    """LeetCode level-order notation, e.g. [1, None, 2, 3]; children of None take no slots."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        for side in ("left", "right"):
            if i < len(values) and values[i] is not None:
                child = TreeNode(values[i])
                setattr(node, side, child)
                queue.append(child)
            i += 1
    return root


def tree_to_list(root: Optional[TreeNode]) -> List:
    """Inverse of build_tree, with trailing None trimmed."""
    values = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node is None:
            values.append(None)
            continue
        values.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while values and values[-1] is None:
        values.pop()
    return values
