from typing import Optional

from helpers import ListNode


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        current = head
        last = head
        count = 0  # the total len of linked list
        while current:
            count += 1
            last = current
            current = current.next
        if count <= 1:  # Notice: remember to check input range
            return head
        # make it a cycle
        last.next = head

        # count from the start
        current = head
        k %= count
        target = count - k
        count = 0
        ans: Optional[ListNode] = None
        while current:
            count += 1
            if count == target:
                ans = current.next
                current.next = None
                break
            current = current.next  # Notice: Do not forget transfer current
        return ans
