from typing import Optional

from helpers import ListNode


class Solution:
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
