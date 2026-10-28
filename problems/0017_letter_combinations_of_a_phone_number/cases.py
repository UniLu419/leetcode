METHOD = "letterCombinations"
UNORDERED = True

CASES = [
    dict(args=('23',), expected=['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']),
    dict(args=('2',), expected=['a', 'b', 'c']),
    # 空串返回空列表，不是 [""]
    dict(args=('',), expected=[]),
    # 7 和 9 各有 4 个字母
    dict(args=('7',), expected=['p', 'q', 'r', 's']),
    dict(args=('79',), expected=['pw', 'px', 'py', 'pz', 'qw', 'qx', 'qy', 'qz', 'rw', 'rx', 'ry', 'rz', 'sw', 'sx', 'sy', 'sz']),
]
