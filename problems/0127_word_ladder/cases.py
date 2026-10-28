import random

METHOD = "ladderLength"

CASES = [
    dict(args=('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog'],), expected=5),
    dict(args=('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log'],), expected=0),
    # 一步可达，且 beginWord 也在列表里
    dict(args=('a', 'c', ['a', 'b', 'c'],), expected=2),
    # endWord 在列表里但不连通
    dict(args=('hot', 'dog', ['hot', 'dog'],), expected=0),
    dict(args=('hot', 'dog', ['hot', 'dog', 'dot'],), expected=3),
]


def bench():
    # 从 "aaaaa" 出发每次改一个字母生成新词，图是连通的且最短路较长
    rng = random.Random(0)
    letters = "abcdefghijklmnopqrstuvwxyz"
    words, seen = ["aaaaa"], {"aaaaa"}
    while len(words) < 5001:
        w = list(rng.choice(words))
        w[rng.randrange(5)] = rng.choice(letters)
        w = "".join(w)
        if w not in seen:
            seen.add(w)
            words.append(w)
    return ("aaaaa", words[-1], words[1:])
