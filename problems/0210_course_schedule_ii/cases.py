import random

METHOD = "findOrder"


def check(output, expected, args):
    """Any order that lists every course once with each prerequisite first; [] exactly when there is a cycle."""
    n, prerequisites = args
    if expected == []:
        return output == []
    if output is None or sorted(output) != list(range(n)):
        return False
    pos = {course: i for i, course in enumerate(output)}
    return all(pos[b] < pos[a] for a, b in prerequisites)


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
    dict(args=(2, [[1, 0]],), expected=[0, 1]),
    dict(args=(4, [[1, 0], [2, 0], [3, 1], [3, 2]],), expected=[0, 2, 1, 3]),
    dict(args=(1, [],), expected=[0]),
    dict(args=(2, [[1, 0], [0, 1]],), expected=[]),
    dict(args=(3, [],), expected=[0, 1, 2]),
    dict(args=(3, [[0, 1], [1, 2]],), expected=[2, 1, 0]),
    dict(args=(4, [[1, 0], [2, 1], [1, 2], [3, 0]],), expected=[]),
]


def bench():
    rng = random.Random(0)
    return (2000, layered_dag(rng, 200, 10, 10000))
