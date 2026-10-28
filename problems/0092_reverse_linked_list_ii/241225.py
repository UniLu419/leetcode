from typing import Optional

from helpers import ListNode


class Solution:
    # 也可以用栈来做，需要反转的地方入栈，然后出栈接上
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if not head:
            return None
        temp = []
        left -= 1
        right -= 1
        while head:
            temp.append(head)
            head = head.next
        while left < right:
            self.switch(temp, left, right)
            left += 1
            right -= 1
        return temp[0]

    def switch(self, array: list[ListNode], left: int, right: int):
        array[left], array[right] = array[right], array[left]
        if left - 1 >= 0:
            array[left - 1].next = array[left]
        array[left].next = array[left + 1]
        array[right - 1].next = array[right]
        if right + 1 < len(array):
            array[right].next = array[right + 1]
        else:
            array[right].next = None
