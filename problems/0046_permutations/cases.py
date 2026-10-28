METHOD = "permute"

CASES = [
    dict(args=([1, 2, 3],), expected=[[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    dict(args=([0, 1],), expected=[[0, 1], [1, 0]]),
    dict(args=([1],), expected=[[1]]),
    # 负数
    dict(args=([-1, 2, -3],), expected=[[-1, 2, -3], [-1, -3, 2], [2, -1, -3], [2, -3, -1], [-3, 2, -1], [-3, -1, 2]]),
]


def check(output, expected, args):
    # 排列之间顺序任意，但每个排列内部的顺序有意义
    return sorted(map(tuple, output)) == sorted(map(tuple, expected))
