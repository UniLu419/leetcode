import random

METHOD = "canJump"

CASES = [
    dict(args=([2, 3, 1, 1, 4],), expected=True),
    dict(args=([3, 2, 1, 0, 4],), expected=False),
    dict(args=([0],), expected=True),
    dict(args=([0, 1],), expected=False),
    dict(args=([2, 0, 0],), expected=True),
    dict(args=([1, 0, 1, 0],), expected=False),
]


def bench():
    # 每个位置最远只能跳到倒数第二格, 终点不可达
    rng = random.Random(0)
    n = 10_000
    return ([rng.randint(1, n - 2 - i) for i in range(n - 2)] + [0, 0],)
