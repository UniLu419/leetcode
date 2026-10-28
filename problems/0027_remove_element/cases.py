METHOD = "removeElement"


def check(output, expected, args):
    return output == len(expected) and sorted(args[0][:output]) == sorted(expected)


CASES = [
    dict(args=([3, 2, 2, 3], 3), expected=[2, 2]),
    dict(args=([0, 1, 2, 2, 3, 0, 4, 2], 2), expected=[0, 1, 3, 0, 4]),
    dict(args=([], 1), expected=[]),
    dict(args=([1], 1), expected=[]),
    dict(args=([4, 4, 4], 4), expected=[]),
    dict(args=([1, 2, 3], 5), expected=[1, 2, 3]),
]
