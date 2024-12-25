from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    head = [1, 2]
                    k = 2
                case 2:
                    # sample 2
                    head = [1, 2, 3, 4, 5]
                    k = 2
                case 3:
                    # sample 3
                    head = [1, 2, 3, 4, 5]
                    k = 3
                case _:
                    break
            imput_head = ListNode(head[0])
            current = imput_head
            for i in range(1, len(head)):
                temp = ListNode(head[i])
                current.next = temp
                current = temp
            ans_head = solution.reverseKGroup(imput_head, k)
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
