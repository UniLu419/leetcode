import random

METHOD = "maximalSquare"

CASES = [
    dict(args=([['1', '0', '1', '0', '0'], ['1', '0', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['1', '0', '0', '1', '0']],), expected=4),
    dict(args=([['0', '1'], ['1', '0']],), expected=1),
    dict(args=([['0']],), expected=0),
    dict(args=([['1']],), expected=1),
    dict(args=([['1', '1', '1', '1'], ['1', '1', '1', '1']],), expected=4),
    dict(args=([['1', '1', '1'], ['1', '1', '1'], ['0', '1', '1']],), expected=4),
    dict(args=([['1', '1', '1', '1', '0'], ['1', '1', '1', '1', '0'], ['1', '1', '1', '1', '1'], ['1', '1', '1', '1', '1'], ['0', '0', '1', '1', '1']],), expected=16),
]


def bench():
    rng = random.Random(0)
    return ([['0' if rng.random() < 0.01 else '1' for _ in range(300)] for _ in range(300)],)
