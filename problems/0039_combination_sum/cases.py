METHOD = "combinationSum"
UNORDERED = True

CASES = [
    dict(args=([2, 3, 6, 7], 7,), expected=[[2, 2, 3], [7]]),
    dict(args=([2, 3, 5], 8,), expected=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
    dict(args=([2], 1,), expected=[]),
    # 只有一个数且正好等于 target
    dict(args=([5], 5,), expected=[[5]]),
    # 所有候选都比 target 大
    dict(args=([3, 4], 2,), expected=[]),
    # 候选未排序；同一个数可重复用，但 [3, 4, 4] 和 [4, 3, 4] 算同一组
    dict(args=([8, 7, 4, 3], 11,), expected=[[3, 4, 4], [3, 8], [4, 7]]),
]
