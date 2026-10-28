import random

METHOD = "containsNearbyDuplicate"

CASES = [
    dict(args=([1, 2, 3, 1], 3), expected=True),
    dict(args=([1, 0, 1, 1], 1), expected=True),
    dict(args=([1, 2, 3, 1, 2, 3], 2), expected=False),
    dict(args=([1], 0), expected=False),
    dict(args=([1, 1], 0), expected=False),
    dict(args=([99, 99], 2), expected=True),
    dict(args=([1, 2, 1], 1), expected=False),
]


def bench():
    return (random.Random(0).sample(range(-10**9, 10**9), 100_000), 100_000)
