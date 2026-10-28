# Definition for singly-linked list.
from typing import Optional

from helpers import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current is not None:
            next_node = current.next
            if next_node is not None:
                if next_node.val == current.val:
                    current.next = next_node.next
                    continue
            current = current.next
        return head
