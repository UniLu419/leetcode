METHOD = "summaryRanges"

CASES = [
    dict(args=([0, 1, 2, 4, 5, 7],), expected=["0->2", "4->5", "7"]),
    dict(args=([0, 2, 3, 4, 6, 8, 9],), expected=["0", "2->4", "6", "8->9"]),
    dict(args=([],), expected=[]),
    dict(args=([-1],), expected=["-1"]),
    dict(args=([1, 3, 5],), expected=["1", "3", "5"]),
    dict(args=([-2147483648, -2147483647, 2147483647],), expected=["-2147483648->-2147483647", "2147483647"]),
]
