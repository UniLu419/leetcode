import random

METHOD = "singleNumber"

CASES = [
    dict(args=([2, 2, 3, 2],), expected=3),
    dict(args=([0, 1, 0, 1, 0, 1, 99],), expected=99),
    dict(args=([5],), expected=5),
    dict(args=([-2, -2, 1, 1, 4, 1, 4, 4, -4, -2],), expected=-4),
    dict(args=([-2147483648, -2147483648, -2147483648, 2147483647],), expected=2147483647),
    dict(args=([2147483647, 2147483647, 2147483647, -2147483648],), expected=-2147483648),
]


def bench():
    rng = random.Random(0)
    values = rng.sample(range(-2**31, 2**31), 10000)
    nums = values[1:] * 3 + [values[0]]
    rng.shuffle(nums)
    return (nums,)
