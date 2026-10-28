from helpers import build_linked_list

METHOD = "addTwoNumbers"

CASES = [
    dict(args=(build_linked_list([2, 4, 3]), build_linked_list([5, 6, 4])), expected=[7, 0, 8]),
    dict(args=(build_linked_list([0]), build_linked_list([0])), expected=[0]),
    dict(
        args=(build_linked_list([9, 9, 9, 9, 9, 9, 9]), build_linked_list([9, 9, 9, 9])),
        expected=[8, 9, 9, 9, 0, 0, 0, 1],
    ),
    dict(args=(build_linked_list([5]), build_linked_list([5])), expected=[0, 1]),
    dict(args=(build_linked_list([1, 8]), build_linked_list([0])), expected=[1, 8]),
    dict(args=(build_linked_list([0]), build_linked_list([7, 3])), expected=[7, 3]),
]
