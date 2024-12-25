from typing import List, Optional
from timing_dec import timing


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next: Optional[ListNode] = next


class Solution:
    @timing
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ans = head
        aim_parent = None
        aim_parent_count = 0
        count = 0
        # find the parent of the node to remove
        while head:
            count += 1
            # calculate parent count to find
            cur_aim_parent_cout = count - n
            # check if need to go next
            if cur_aim_parent_cout > aim_parent_count:
                if aim_parent_count == 0:
                    aim_parent = ans
                else:
                    aim_parent = aim_parent.next
                aim_parent_count += 1
            head = head.next

        # remove found
        if aim_parent:
            aim_parent.next = aim_parent.next.next
        else:
            ans = ans.next
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
            print(f"ans = {solution.removeNthFromEnd(k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
