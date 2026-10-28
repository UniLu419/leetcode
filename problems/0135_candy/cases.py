import random

METHOD = "candy"

CASES = [
    dict(args=([1, 0, 2],), expected=5),
    dict(args=([1, 2, 2],), expected=4),
    dict(args=([1],), expected=1),
    dict(args=([1, 3, 4, 5, 2],), expected=11),
    dict(args=([1, 2, 87, 87, 87, 2, 1],), expected=13),
    dict(args=([5, 5, 5],), expected=3),
]


def bench():
    rng = random.Random(0)
    return ([rng.randint(0, 2 * 10**4) for _ in range(20_000)],)
