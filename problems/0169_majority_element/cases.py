import random

METHOD = "majorityElement"

CASES = [
    dict(args=([3, 2, 3],), expected=3),
    dict(args=([2, 2, 1, 1, 1, 2, 2],), expected=2),
    dict(args=([1],), expected=1),
    dict(args=([-1, -1, 2],), expected=-1),
    dict(args=([5, 5, 5, 5],), expected=5),
    dict(args=([6, 5, 5],), expected=5),
]


def bench():
    rng = random.Random(0)
    nums = [7] * 25_001 + [rng.randint(-10**9, 10**9) for _ in range(24_999)]
    rng.shuffle(nums)
    return (nums,)
