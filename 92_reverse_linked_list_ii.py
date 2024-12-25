from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    # 也可以用栈来做，需要反转的地方入栈，然后出栈接上
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    k = 3
                case 2:
                    # sample 2
                    k = 2
                case 3:
                    # sample 3
                    k = 3
                case _:
                    break
            print(f"ans = {solution.solve(k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
