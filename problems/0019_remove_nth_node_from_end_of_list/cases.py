from helpers import build_linked_list

METHOD = "removeNthFromEnd"

# An empty result list is None, so its expected value is written as None.
CASES = [
    dict(args=(build_linked_list([1, 2, 3, 4, 5]), 2), expected=[1, 2, 3, 5]),
    dict(args=(build_linked_list([1]), 1), expected=None),
    dict(args=(build_linked_list([1, 2]), 1), expected=[1]),
    dict(args=(build_linked_list([1, 2]), 2), expected=[2]),
    dict(args=(build_linked_list([1, 2, 3]), 3), expected=[2, 3]),
]
