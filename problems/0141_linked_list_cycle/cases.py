import random

from helpers import build_linked_list

METHOD = "hasCycle"


def build_cycle(values, pos):
    """LeetCode input: the tail links back to the node at index pos (-1 means no cycle)."""
    head = build_linked_list(values)
    if pos >= 0:
        tail, target, i = head, None, 0
        while True:
            if i == pos:
                target = tail
            if tail.next is None:
                break
            tail, i = tail.next, i + 1
        tail.next = target
    return head


CASES = [
    dict(args=(build_cycle([3, 2, 0, -4], 1),), expected=True),
    dict(args=(build_cycle([1, 2], 0),), expected=True),
    dict(args=(build_cycle([1], -1),), expected=False),
    dict(args=(build_cycle([], -1),), expected=False),
    dict(args=(build_cycle([1, 1, 1], 2),), expected=True),
    dict(args=(build_cycle([1, 2, 3, 4], -1),), expected=False),
]


def bench():
    rng = random.Random(0)
    n = 10_000
    return (build_cycle([rng.randint(-(10**5), 10**5) for _ in range(n)], rng.randint(0, n - 1)),)
