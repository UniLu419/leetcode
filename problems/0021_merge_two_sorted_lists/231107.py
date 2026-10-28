from typing import Optional

from helpers import ListNode


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        ans: Optional[ListNode] = None
        current: Optional[ListNode] = None
        while list1 and list2:
            if list1.val < list2.val:
                if current:
                    current.next = list1
                    list1 = list1.next
                    current = current.next
                else:
                    ans = list1
                    current = ans
                    list1 = list1.next
            else:
                if current:
                    current.next = list2
                    list2 = list2.next
                    current = current.next
                else:
                    ans = list2
                    current = ans
                    list2 = list2.next
        if list1:
            if current:
                current.next = list1
            else:
                ans = list1
                current = list1
        if list2:
            if current:
                current.next = list2
            else:
                ans = list2
                current = list2
        return ans
