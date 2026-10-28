from typing import Optional

from helpers import ListNode


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        stack = []
        if not head:
            return None
        ans: Optional[ListNode] = None
        current: Optional[ListNode] = None
        while head:
            stack.append(head)
            next = head.next
            if len(stack) == k:
                while stack:
                    temp = stack.pop()
                    if not ans:
                        ans = temp
                        current = ans
                    else:
                        current.next = temp
                        current = temp
            head = next
        if stack:
            current.next = stack[0]
        else:
            current.next = None  # 不要忘记处理最后一个数的next
        return ans
