import random

METHOD = "removeDuplicates"


def check(output, expected, args):
    return output == len(expected) and args[0][:output] == expected


CASES = [
    dict(args=([1, 1, 2],), expected=[1, 2]),
    dict(args=([0, 0, 1, 1, 1, 2, 2, 3, 3, 4],), expected=[0, 1, 2, 3, 4]),
    dict(args=([1],), expected=[1]),
    dict(args=([2, 2, 2],), expected=[2]),
    dict(args=([-3, -1, 0, 5],), expected=[-3, -1, 0, 5]),
]


def bench():
    rng = random.Random(0)
    return (sorted(rng.randint(-100, 100) for _ in range(30_000)),)
