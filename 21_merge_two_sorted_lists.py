from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    @timing
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
