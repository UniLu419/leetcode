from helpers import build_linked_list

METHOD = "deleteDuplicates"

CASES = [
    dict(args=(build_linked_list([1, 2, 3, 3, 4, 4, 5]),), expected=[1, 2, 5]),
    dict(args=(build_linked_list([1, 1, 1, 2, 3]),), expected=[2, 3]),
    dict(args=(build_linked_list([]),), expected=None),
    dict(args=(build_linked_list([1]),), expected=[1]),
    dict(args=(build_linked_list([1, 1]),), expected=None),
    dict(args=(build_linked_list([1, 2, 2]),), expected=[1]),
    dict(args=(build_linked_list([-1, -1, 0, 0]),), expected=None),
]
