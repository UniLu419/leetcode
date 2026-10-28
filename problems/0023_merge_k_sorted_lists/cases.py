import random

from helpers import build_linked_list

METHOD = "mergeKLists"

# An empty result list is None, so its expected value is written as None.
CASES = [
    dict(args=([build_linked_list([1, 4, 5]), build_linked_list([1, 3, 4]), build_linked_list([2, 6])],), expected=[1, 1, 2, 3, 4, 4, 5, 6]),
    dict(args=([],), expected=None),
    dict(args=([build_linked_list([])],), expected=None),
    dict(args=([build_linked_list([]), build_linked_list([1])],), expected=[1]),
    dict(args=([build_linked_list([1, 2, 3])],), expected=[1, 2, 3]),
    dict(args=([build_linked_list([-2, -1, -1]), build_linked_list([-1, 0]), build_linked_list([-3])],), expected=[-3, -2, -1, -1, -1, 0]),
    dict(args=([build_linked_list([-10000, 10000]), build_linked_list([-10000])],), expected=[-10000, -10000, 10000]),
]


def bench():
    rng = random.Random(0)
    return ([build_linked_list(sorted(rng.randint(-10**4, 10**4) for _ in range(10))) for _ in range(1000)],)
