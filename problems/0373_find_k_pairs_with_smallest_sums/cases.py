import random
from collections import Counter

METHOD = "kSmallestPairs"

CASES = [
    dict(args=([1, 7, 11], [2, 4, 6], 3,), expected=[[1, 2], [1, 4], [1, 6]]),
    dict(args=([1, 1, 2], [1, 2, 3], 2,), expected=[[1, 1], [1, 1]]),
    dict(args=([5], [-3], 1), expected=[[5, -3]]),
    dict(args=([1, 2], [3], 2), expected=[[1, 3], [2, 3]]),
    dict(args=([-10, -4, 0, 0, 6], [3, 5, 6, 7, 8, 100], 10),
         expected=[[-10, 3], [-10, 5], [-10, 6], [-10, 7], [-10, 8], [-4, 3], [-4, 5], [-4, 6], [-4, 7], [0, 3]]),
    dict(args=([1, 1, 2], [1, 2, 3], 9),
         expected=[[1, 1], [1, 1], [1, 2], [1, 2], [2, 1], [1, 3], [1, 3], [2, 2], [2, 3]]),
]


def check(output, expected, args):
    """Any k pairs with the k smallest sums are accepted, in any order among equal sums."""
    nums1, nums2, _ = args
    if not isinstance(output, list) or len(output) != len(expected):
        return False
    if not all(isinstance(p, (list, tuple)) and len(p) == 2 for p in output):
        return False
    have1, have2 = Counter(nums1), Counter(nums2)
    used = Counter((u, v) for u, v in output)
    if any(count > have1[u] * have2[v] for (u, v), count in used.items()):
        return False
    return sorted(u + v for u, v in output) == sorted(u + v for u, v in expected)


def bench():
    rng = random.Random(0)
    nums1 = sorted(rng.randint(-10**9, 10**9) for _ in range(10**5))
    nums2 = sorted(rng.randint(-10**9, 10**9) for _ in range(10**5))
    return (nums1, nums2, 10**4)
