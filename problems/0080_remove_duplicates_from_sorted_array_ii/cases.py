import random

METHOD = "removeDuplicates"

CASES = [
    dict(args=([1, 1, 1, 2, 2, 3],), expected=[1, 1, 2, 2, 3]),
    dict(args=([0, 0, 1, 1, 1, 1, 2, 3, 3],), expected=[0, 0, 1, 1, 2, 3, 3]),
    dict(args=([1],), expected=[1]),
    dict(args=([1, 1],), expected=[1, 1]),
    dict(args=([2, 2, 2, 2],), expected=[2, 2]),
    dict(args=([-3, -3, -3, -1, 0, 0, 0],), expected=[-3, -3, -1, 0, 0]),
]


def check(output, expected, args):
    """Returns k; the first k elements of nums must equal expected."""
    return output == len(expected) and args[0][:output] == expected


def bench():
    rng = random.Random(0)
    return (sorted(rng.randint(-(10**4), 10**4) for _ in range(30_000)),)
