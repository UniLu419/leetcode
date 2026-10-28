import random

METHOD = "canCompleteCircuit"

CASES = [
    dict(args=([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]), expected=3),
    dict(args=([2, 3, 4], [3, 4, 3]), expected=-1),
    dict(args=([5, 1, 2, 3, 4], [4, 4, 1, 5, 1]), expected=4),
    dict(args=([5, 1], [1, 5]), expected=0),
    dict(args=([2], [2]), expected=0),
    dict(args=([1], [2]), expected=-1),
    dict(args=([3, 1, 1], [1, 2, 2]), expected=0),
]


def bench():
    # Alternating +1/-1 keeps most starts alive until the big drop at n-2; the only valid start is n-1.
    rng = random.Random(0)
    n = 100_000
    diff = [1 if i % 2 == 0 else -1 for i in range(n - 2)] + [-5000, 5000]
    base = [rng.randint(0, 5000) for _ in range(n)]
    gas = [b + max(d, 0) for b, d in zip(base, diff)]
    cost = [b + max(-d, 0) for b, d in zip(base, diff)]
    return (gas, cost)
