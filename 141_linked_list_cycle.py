from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next: Optional[ListNode] = None


class Solution:
    @timing
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 利用地址hash
        hash_map = {}
        current = head
        while current:
            current_id = id(current)
            if current_id not in hash_map:
                hash_map[current_id] = True
            else:
                return True
            current = current.next
        return False

    @timing
    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        # 利用不同步长
        fast: Optional[ListNode] = head
        slow: Optional[ListNode] = head
        while fast and fast.next:
            slow = slow.next  # type: ignore
            fast = fast.next.next
            if slow == fast:
                return True
        return False


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    heads = [3, 2, 0, -4]
                    pos = 1
                case 2:
                    # sample 2
                    heads = [1, 2]
                    pos = 0
                case 3:
                    # sample 3
                    heads = [1]
                    pos = -1
                case _:
                    break
            input_head = ListNode(heads[0])
            cycle: Optional[ListNode] = None
            if pos == 0:
                cycle = input_head
            current = input_head
            for i in range(1, len(heads)):
                temp = ListNode(heads[i])
                if i == pos:
                    cycle = temp
                current.next = temp
                current = temp
            current.next = cycle

            print(f"ans = {solution.hasCycle(input_head)}")
            print(f"ans = {solution.hasCycle2(input_head)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
