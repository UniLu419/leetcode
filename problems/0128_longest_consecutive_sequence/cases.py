import random

METHOD = "longestConsecutive"

CASES = [
    dict(args=([100, 4, 200, 1, 3, 2],), expected=4),
    dict(args=([0, 3, 7, 2, 5, 8, 4, 6, 0, 1],), expected=9),
    dict(args=([1, 0, 1, 2],), expected=3),
    dict(args=([],), expected=0),
    dict(args=([-1, -2, -3, 5],), expected=3),
    dict(args=([7, 7, 7],), expected=1),
]


def bench():
    # One long run where every value appears twice.
    nums = list(range(50_000)) * 2
    random.Random(0).shuffle(nums)
    return (nums,)
