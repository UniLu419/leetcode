import random

METHOD = "singleNumber"

CASES = [
    dict(args=([2, 2, 1],), expected=1),
    dict(args=([4, 1, 2, 1, 2],), expected=4),
    dict(args=([1],), expected=1),
    dict(args=([7, -3, 7],), expected=-3),
    dict(args=([30000, -30000, 30000],), expected=-30000),
    dict(args=([0, 5, 5],), expected=0),
]


def bench():
    rng = random.Random(0)
    values = rng.sample(range(-30000, 30001), 15000)
    nums = values[1:] * 2 + [values[0]]
    rng.shuffle(nums)
    return (nums,)
