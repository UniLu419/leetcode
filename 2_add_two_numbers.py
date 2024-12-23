from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    l1 = [2, 4, 3]
                    l2 = [5, 6, 4]
                case 2:
                    # sample 2
                    l1 = [0]
                    l2 = [0]
                case 3:
                    # sample 3
                    l1 = [9, 9, 9, 9, 9, 9, 9]
                    l2 = [9, 9, 9, 9]
                case _:
                    break
            l1_head = ListNode(l1[0])
            current = l1_head
            for i in range(1, len(l1)):
                temp = ListNode(l1[i])
                current.next = temp
                current = temp
            l2_head = ListNode(l2[0])
            current = l2_head
            for i in range(1, len(l2)):
                temp = ListNode(l2[i])
                current.next = temp
                current = temp
            ans_head = solution.addTwoNumbers(l1_head, l2_head)
            ans = []
            while ans_head:
                ans.append(ans_head.val)
                ans_head.next
            print(f"ans = {ans}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
