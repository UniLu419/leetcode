import random

CLASS = "LRUCache"

CASES = [
    dict(ops=['LRUCache', 'put', 'put', 'get', 'put', 'get', 'put', 'get', 'get', 'get'], args=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]], expected=[None, None, None, 1, None, -1, None, -1, 3, 4]),
    dict(ops=['LRUCache', 'put', 'get', 'put', 'get', 'get'], args=[[1], [2, 1], [2], [3, 2], [2], [3]], expected=[None, None, 1, None, -1, 2]),
    dict(ops=['LRUCache', 'put', 'put', 'put', 'put', 'get', 'get', 'get'], args=[[2], [1, 1], [2, 2], [1, 10], [3, 3], [1], [2], [3]], expected=[None, None, None, None, None, 10, -1, 3]),
    dict(ops=['LRUCache', 'put', 'put', 'get', 'put', 'get', 'get', 'get'], args=[[2], [1, 1], [2, 2], [1], [3, 3], [2], [1], [3]], expected=[None, None, None, 1, None, -1, 1, 3]),
    dict(ops=['LRUCache', 'get', 'put', 'get'], args=[[2], [1], [1, 0], [1]], expected=[None, -1, None, 0]),
]


def bench():
    rng = random.Random(0)
    ops, args = ["LRUCache"], [[3000]]
    for _ in range(200_000):
        key = rng.randint(0, 10**4)
        if rng.random() < 0.5:
            ops.append("get")
            args.append([key])
        else:
            ops.append("put")
            args.append([key, rng.randint(0, 10**5)])
    return (ops, args)
