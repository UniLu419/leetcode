from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    head = [1, 2, 3, 4, 5]
                    k = 2
                case 2:
                    # sample 2
                    head = [0, 1, 2]
                    k = 4
                case _:
                    break
            imput_head = ListNode(head[0])
            current = imput_head
            for i in range(1, len(head)):
                temp = ListNode(head[i])
                current.next = temp
                current = temp
            ans_head = solution.rotateRight(imput_head, k)
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
