from typing import Optional
from helpers import ListNode


class Solution:
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
