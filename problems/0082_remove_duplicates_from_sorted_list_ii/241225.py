from typing import Optional

from helpers import ListNode


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans: Optional[ListNode] = None
        current: Optional[ListNode] = None
        if not head or not head.next:
            return head
        while head:
            if head.next and head.val == head.next.val:
                standard = head.val
                # Notice: set current.next to delete the following node if there is any current
                if current:
                    current.next = None
                # remove all duplicated head(from head one by one)
                while head and head.val == standard:
                    head = head.next
            else:
                if current:
                    current.next = head
                    current = head
                else:
                    ans = head
                    current = ans
                head = head.next
        return ans
