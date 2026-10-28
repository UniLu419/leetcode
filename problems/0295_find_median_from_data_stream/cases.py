import random

CLASS = "MedianFinder"

CASES = [
    dict(ops=['MedianFinder', 'addNum', 'addNum', 'findMedian', 'addNum', 'findMedian'], args=[[], [1], [2], [], [3], []], expected=[None, None, None, 1.5, None, 2.0]),
    dict(ops=['MedianFinder', 'addNum', 'findMedian'], args=[[], [-100000], []], expected=[None, None, -100000.0]),
    dict(ops=['MedianFinder', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian'],
         args=[[], [-1], [], [-2], [], [-3], [], [-4], [], [-5], []],
         expected=[None, None, -1.0, None, -1.5, None, -2.0, None, -2.5, None, -3.0]),
    dict(ops=['MedianFinder', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian', 'addNum', 'findMedian'],
         args=[[], [6], [], [10], [], [2], [], [6], [], [5], [], [0], []],
         expected=[None, None, 6.0, None, 8.0, None, 6.0, None, 6.0, None, 6.0, None, 5.5]),
]


def bench():
    rng = random.Random(0)
    ops, args = ["MedianFinder"], [[]]
    for _ in range(25_000):
        ops += ["addNum", "findMedian"]
        args += [[rng.randint(-10**5, 10**5)], []]
    return (ops, args)
