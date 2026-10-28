import random

METHOD = "findWords"
UNORDERED = True

CASES = [
    dict(args=([['o', 'a', 'a', 'n'], ['e', 't', 'a', 'e'], ['i', 'h', 'k', 'r'], ['i', 'f', 'l', 'v']], ['oath', 'pea', 'eat', 'rain'],), expected=['eat', 'oath']),
    dict(args=([['a', 'b'], ['c', 'd']], ['abcb'],), expected=[]),
    # 单格棋盘
    dict(args=([['a']], ['a'],), expected=['a']),
    # 同一格不能重复用；共享前缀的单词都要找出
    dict(args=([['a', 'a']], ['a', 'aa', 'aaa'],), expected=['a', 'aa']),
    # 一个单词有多条路径时只输出一次
    dict(args=([['a', 'b'], ['b', 'a']], ['ab', 'ba', 'aba', 'abab', 'b'],), expected=['ab', 'aba', 'abab', 'b', 'ba']),
]


def bench():
    rng = random.Random(0)
    m = n = 12
    board = [[rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(n)] for _ in range(m)]
    words = set()
    # 一半是棋盘上真实存在的路径，一半是随机串
    while len(words) < 15_000:
        r, c = rng.randrange(m), rng.randrange(n)
        seen, w = {(r, c)}, [board[r][c]]
        for _ in range(rng.randint(0, 9)):
            nxt = [(r + dr, c + dc) for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1))
                   if 0 <= r + dr < m and 0 <= c + dc < n and (r + dr, c + dc) not in seen]
            if not nxt:
                break
            r, c = rng.choice(nxt)
            seen.add((r, c))
            w.append(board[r][c])
        words.add("".join(w))
    while len(words) < 30_000:
        words.add("".join(rng.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(rng.randint(1, 10))))
    return (board, sorted(words))
