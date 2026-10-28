from helpers import build_linked_list

METHOD = "mergeTwoLists"

# An empty result list is None, so its expected value is written as None.
CASES = [
    dict(args=(build_linked_list([1, 2, 4]), build_linked_list([1, 3, 4])), expected=[1, 1, 2, 3, 4, 4]),
    dict(args=(build_linked_list([]), build_linked_list([])), expected=None),
    dict(args=(build_linked_list([]), build_linked_list([0])), expected=[0]),
    dict(args=(build_linked_list([5]), build_linked_list([1, 2, 4])), expected=[1, 2, 4, 5]),
    dict(args=(build_linked_list([1, 1]), build_linked_list([1])), expected=[1, 1, 1]),
    dict(args=(build_linked_list([-3, 0]), build_linked_list([-2])), expected=[-3, -2, 0]),
]
