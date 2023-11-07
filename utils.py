from typing import List, Optional
from custom_types import ListNode
import re


def string_to_int_list(int_str: str) -> List[int]:
    """
    This is a function for parsing a string to int list
    The integers should be separated by single space

    Args:
        s (str): the string to parse

    Returns:
        List[int]: the parsed integer list

    Usage:
    string_to_int_list("0 1")
    """
    try:
        int_str = re.sub(r"[^0-9]", "", int_str)
        int_str = re.sub(r" +", " ", int_str)
        int_str_list = int_str.split()
        int_list = []
        for s in int_str_list:
            int_list.append(int(s))
        return int_list

    except Exception as e:
        print("Parsing string to int list failed: ", e)


def string_to_single_linked_list(int_str: str) -> Optional[ListNode]:
    """
    This is a function for parsing a string to a int single linked list
    integers should be separated by single space

    Args:
        s (str): the string to parse

    Returns:
        Optional[ListNode]: the header of this int single linked list.

    Usage:
    string_to_single_linked_list("0 1")
    """
    try:
        int_list = string_to_int_list(int_str)
        return create_single_linked_list(int_list)

    except Exception as e:
        print("Parsing string to single linked list failed: ", e)


def create_single_linked_list(int_list: List[int]) -> Optional[ListNode]:
    """
    This is a function for parsing a int list to a int single linked list

    Args:
        int_list (List[int]): the int list to parse

    Returns:
        Optional[ListNode]: the header of this int single linked list

    Usage:
    create_single_linked_list([0, 1])
    """
    try:
        if len(int_list) < 1:
            return None
        head: ListNode = None
        current: ListNode
        for x in int_list:
            temp = ListNode(x)
            if head is None:
                head = temp
                current = temp
                continue
            current.next = temp
            current = temp
        return head

    except Exception as e:
        print("Creating single linked list failed: ", e)


def print_single_linked_list(head: Optional[ListNode]) -> None:
    """
    This is a function for printing a int single linked list

    Args:
        head (Optional[ListNode]): the header of this int single linked list

    Usage:
    print_single_linked_list([0, 1])
    """
    try:
        current = head
        output_str = ""
        while current is not None:
            output_str += f" {current.val}"
            current = current.next
        print(output_str.strip())

    except Exception as e:
        print("Parsing string to single linked list failed: ", e)
