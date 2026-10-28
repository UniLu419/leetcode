import random

CLASS = "MinStack"

CASES = [
    dict(
        ops=["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"],
        args=[[], [-2], [0], [-3], [], [], [], []],
        expected=[None, None, None, None, -3, None, 0, -2],
    ),
    dict(
        ops=["MinStack", "push", "top", "getMin"],
        args=[[], [5], [], []],
        expected=[None, None, 5, 5],
    ),
    dict(
        ops=["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"],
        args=[[], [0], [1], [0], [], [], [], [], []],
        expected=[None, None, None, None, 0, None, 0, None, 0],
    ),
    dict(
        ops=["MinStack", "push", "push", "getMin", "pop", "getMin", "top"],
        args=[[], [2147483647], [-2147483648], [], [], [], []],
        expected=[None, None, None, -2147483648, None, 2147483647, 2147483647],
    ),
]


def bench():
    rng = random.Random(0)
    ops, args, size = ["MinStack"], [[]], 0
    for _ in range(30_000):
        if size == 0 or rng.random() < 0.6:
            ops.append("push")
            args.append([rng.randint(-(2**31), 2**31 - 1)])
            size += 1
        else:
            op = rng.choice(["pop", "top", "getMin"])
            ops.append(op)
            args.append([])
            size -= op == "pop"
    return (ops, args)
