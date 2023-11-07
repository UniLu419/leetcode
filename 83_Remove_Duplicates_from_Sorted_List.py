# Definition for singly-linked list.
from typing import Optional
from custom_types import ListNode
from utils import print_single_linked_list, string_to_single_linked_list


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current is not None:
            next_node = current.next
            if next_node is not None:
                if next_node.val == current.val:
                    current.next = next_node.next
                    continue
            current = current.next
        return head


solution = Solution()
while True:
    try:
        a = input("List: ")
        if a == "q":
            break
        head = string_to_single_linked_list(a)
        head = solution.deleteDuplicates(head)
        print("Single linked list:")
        print_single_linked_list(head)
    except Exception as e:
        print(e)
        break
