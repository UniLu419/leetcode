import random

METHOD = "twoSum"
UNORDERED = True

CASES = [
    dict(args=([2, 7, 11, 15], 9), expected=[0, 1]),
    dict(args=([3, 2, 4], 6), expected=[1, 2]),
    dict(args=([3, 3], 6), expected=[0, 1]),
    dict(args=([-1, -2, -3, -4, -5], -8), expected=[2, 4]),
    dict(args=([0, 4, 3, 0], 0), expected=[0, 3]),
]


def bench():
    nums = random.Random(0).sample(range(1, 10**9), 20_000)
    return (nums, nums[-1] + nums[-2])
