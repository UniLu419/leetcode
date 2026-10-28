from helpers import build_linked_list

METHOD = "partition"

CASES = [
    dict(args=(build_linked_list([1, 4, 3, 2, 5, 2]), 3,), expected=[1, 2, 2, 4, 3, 5]),
    dict(args=(build_linked_list([2, 1]), 2,), expected=[1, 2]),
    dict(args=(build_linked_list([]), 0), expected=None),
    dict(args=(build_linked_list([1, 2, 3]), 5), expected=[1, 2, 3]),
    dict(args=(build_linked_list([5, 4, 3]), 1), expected=[5, 4, 3]),
    dict(args=(build_linked_list([3, -1, 3, -2, 0, 3]), 3), expected=[-1, -2, 0, 3, 3, 3]),
]
