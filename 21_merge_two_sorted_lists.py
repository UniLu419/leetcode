from typing import Optional
from custom_types import ListNode
from utils import string_to_single_linked_list, print_single_linked_list


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        sum_list: Optional[ListNode] = None
        parent: Optional[ListNode] = None
        head1 = list1
        head2 = list2
        while head1 is not None and head2 is not None:
            if head1.val > head2.val:
                current = head2
                head2 = head2.next
            else:
                current = head1
                head1 = head1.next

            if sum_list is None:
                sum_list = current
                parent = current
            else:
                parent.next = current
                parent = current
        if head1 is None:
            if sum_list is None:
                return list2
            else:
                parent.next = head2
                return sum_list
        if head2 is None:
            if sum_list is None:
                return list1
            else:
                parent.next = head1
                return sum_list
        return list


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s1 = input("Please enter list1: ")
            s2 = input("Please enter list2: ")
            list1 = string_to_single_linked_list(s1)
            list2 = string_to_single_linked_list(s2)
            ans = solution.mergeTwoLists(list1, list2)
            print_single_linked_list(ans)
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
