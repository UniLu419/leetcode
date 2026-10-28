from typing import Optional
from helpers import ListNode


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 利用不同步长
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
            if slow == fast:
                return True
        return False
