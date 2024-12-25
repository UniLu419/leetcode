from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    head = [1, 2, 3, 3, 4, 4, 5]
                case 2:
                    # sample 2
                    head = [1, 1, 1, 2, 3]
                case 3:
                    # sample 3
                    head = [1, 2, 2]
                case _:
                    break
            imput_head = ListNode(head[0])
            current = imput_head
            for i in range(1, len(head)):
                temp = ListNode(head[i])
                current.next = temp
                current = temp
            ans_head = solution.deleteDuplicates(imput_head)
            ans = []
            while ans_head:
                ans.append(ans_head.val)
                ans_head = ans_head.next
            print(f"ans = {ans}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
