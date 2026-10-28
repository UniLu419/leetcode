import random

METHOD = "canFinish"


def layered_dag(rng, layers, width, edges):
    """Random DAG over layers * width shuffled course labels; every edge goes from one layer to the next."""
    labels = list(range(layers * width))
    rng.shuffle(labels)
    grid = [labels[i * width:(i + 1) * width] for i in range(layers)]
    pairs = set()
    for i in range(1, layers):
        for course in grid[i]:
            pairs.add((course, rng.choice(grid[i - 1])))
    while len(pairs) < edges:
        i = rng.randrange(1, layers)
        pairs.add((rng.choice(grid[i]), rng.choice(grid[i - 1])))
    prerequisites = [list(p) for p in pairs]
    rng.shuffle(prerequisites)
    return prerequisites


CASES = [
    dict(args=(2, [[1, 0]],), expected=True),
    dict(args=(2, [[1, 0], [0, 1]],), expected=False),
    dict(args=(1, [],), expected=True),
    dict(args=(4, [[1, 0], [2, 0], [3, 1], [3, 2]],), expected=True),
    dict(args=(5, [[1, 0], [3, 2], [4, 3], [2, 4]],), expected=False),
    dict(args=(3, [[0, 1], [1, 2]],), expected=True),
]


def bench():
    rng = random.Random(0)
    return (2000, layered_dag(rng, 200, 10, 5000))
