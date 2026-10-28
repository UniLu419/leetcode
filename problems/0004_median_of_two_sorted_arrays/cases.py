METHOD = "findMedianSortedArrays"

CASES = [
    dict(args=([1, 3], [2],), expected=2.0),
    dict(args=([1, 2], [3, 4],), expected=2.5),
    dict(args=([], [1],), expected=1.0),
    dict(args=([2], [],), expected=2.0),
    dict(args=([1, 1], [1, 1],), expected=1.0),
    dict(args=([-1000000], [1000000],), expected=0.0),
]
