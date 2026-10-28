from helpers import build_linked_list

METHOD = "rotateRight"

CASES = [
    dict(args=(build_linked_list([1, 2, 3, 4, 5]), 2), expected=[4, 5, 1, 2, 3]),
    dict(args=(build_linked_list([0, 1, 2]), 4), expected=[2, 0, 1]),
    dict(args=(build_linked_list([]), 0), expected=None),
    dict(args=(build_linked_list([1]), 99), expected=[1]),
    dict(args=(build_linked_list([1, 2]), 2), expected=[1, 2]),
    dict(args=(build_linked_list([1, 2, 3]), 2_000_000_000), expected=[2, 3, 1]),
]
