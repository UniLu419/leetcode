from helpers import build_linked_list

METHOD = "reverseBetween"

CASES = [
    dict(args=(build_linked_list([1, 2, 3, 4, 5]), 2, 4), expected=[1, 4, 3, 2, 5]),
    dict(args=(build_linked_list([5]), 1, 1), expected=[5]),
    dict(args=(build_linked_list([1, 2]), 1, 2), expected=[2, 1]),
    dict(args=(build_linked_list([1, 2, 3]), 1, 3), expected=[3, 2, 1]),
    dict(args=(build_linked_list([1, 2, 3, 4]), 3, 4), expected=[1, 2, 4, 3]),
    dict(args=(build_linked_list([3, 5]), 2, 2), expected=[3, 5]),
]
