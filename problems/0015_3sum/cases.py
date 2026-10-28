METHOD = "threeSum"
UNORDERED = True

CASES = [
    dict(args=([-1, 0, 1, 2, -1, -4],), expected=[[-1, -1, 2], [-1, 0, 1]]),
    dict(args=([0, 1, 1],), expected=[]),
    dict(args=([0, 0, 0],), expected=[[0, 0, 0]]),
    dict(args=([0, 0, 0, 0],), expected=[[0, 0, 0]]),
    dict(args=([-2, 0, 1, 1, 2],), expected=[[-2, 0, 2], [-2, 1, 1]]),
    dict(args=([1, 2, -2, -1],), expected=[]),
]
