from helpers import build_linked_list

METHOD = "reverseKGroup"

CASES = [
    dict(args=(build_linked_list([1, 2, 3, 4, 5]), 2), expected=[2, 1, 4, 3, 5]),
    dict(args=(build_linked_list([1, 2, 3, 4, 5]), 3), expected=[3, 2, 1, 4, 5]),
    dict(args=(build_linked_list([1]), 1), expected=[1]),
    dict(args=(build_linked_list([1, 2]), 2), expected=[2, 1]),
    dict(args=(build_linked_list([1, 2, 3, 4]), 1), expected=[1, 2, 3, 4]),
    dict(args=(build_linked_list([1, 2, 3, 4, 5, 6]), 3), expected=[3, 2, 1, 6, 5, 4]),
]
