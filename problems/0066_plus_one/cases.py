METHOD = "plusOne"

CASES = [
    dict(args=([1, 2, 3],), expected=[1, 2, 4]),
    dict(args=([4, 3, 2, 1],), expected=[4, 3, 2, 2]),
    dict(args=([9],), expected=[1, 0]),
    dict(args=([0],), expected=[1]),
    dict(args=([9, 9, 9],), expected=[1, 0, 0, 0]),
    dict(args=([1, 9, 9],), expected=[2, 0, 0]),
]
