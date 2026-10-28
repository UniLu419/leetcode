from typing import Optional

from helpers import ListNode


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        current: Optional[ListNode] = None
        ans: Optional[ListNode] = None
        increase = 0
        while l1 and l2:
            a = l1.val
            b = l2.val
            sum = a + b + increase
            increase, value = divmod(sum, 10)
            temp = ListNode(value)
            if not ans:
                ans = temp
            if current:
                current.next = temp
            current = temp
            l1 = l1.next
            l2 = l2.next
        while l1:
            a = l1.val
            sum = a + increase
            increase, value = divmod(sum, 10)
            temp = ListNode(value)
            if current:
                current.next = temp
            current = temp
            l1 = l1.next
        while l2:
            a = l2.val
            sum = a + increase
            increase, value = divmod(sum, 10)
            temp = ListNode(value)
            if current:
                current.next = temp
            current = temp
            l2 = l2.next
        if increase != 0:
            temp = ListNode(increase)
            if current:
                current.next = temp
            current = temp
        return ans
