METHOD = "exist"

CASES = [
    dict(args=([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCCED',), expected=True),
    dict(args=([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'SEE',), expected=True),
    dict(args=([['A', 'B', 'C', 'E'], ['S', 'F', 'C', 'S'], ['A', 'D', 'E', 'E']], 'ABCB',), expected=False),
    # 单格
    dict(args=([['a']], 'a',), expected=True),
    # 单词比棋盘格子还多
    dict(args=([['a']], 'ab',), expected=False),
    # 同一格不能用两次
    dict(args=([['a', 'b']], 'aba',), expected=False),
    # 走错一条路后必须恢复访问标记，否则会漏掉正确路径
    dict(args=([['A', 'B', 'C', 'E'], ['S', 'F', 'E', 'S'], ['A', 'D', 'E', 'E']], 'ABCESEEEFS',), expected=True),
]


def bench():
    # 全是 A 的棋盘找末尾为 B 的长单词：不剪枝的回溯会穷举海量路径
    return ([['A'] * 6 for _ in range(6)], 'A' * 14 + 'B')
