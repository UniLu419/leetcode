import random

CLASS = "WordDictionary"

CASES = [
    dict(ops=['WordDictionary', 'addWord', 'addWord', 'addWord', 'search', 'search', 'search', 'search'], args=[[], ['bad'], ['dad'], ['mad'], ['pad'], ['bad'], ['.ad'], ['b..']], expected=[None, None, None, None, False, True, True, True]),
    # 空字典查 "."；全是点；长度不同不算匹配
    dict(ops=['WordDictionary', 'search', 'addWord', 'search', 'search', 'search', 'search'], args=[[], ['.'], ['a'], ['.'], ['..'], ['a'], ['b']], expected=[None, False, None, True, False, True, False]),
    # 点要试遍所有分支：前缀匹配但不是完整单词时要继续找别的分支
    dict(ops=['WordDictionary', 'addWord', 'addWord', 'search', 'search', 'search', 'search'], args=[[], ['ab'], ['cbd'], ['.b'], ['.bd'], ['..'], ['c.']], expected=[None, None, None, True, True, True, False]),
]


def bench():
    rng = random.Random(0)
    letters = "abcdefghij"
    ops, args = ["WordDictionary"], [[]]
    for _ in range(5_000):
        ops.append("addWord")
        args.append(["".join(rng.choice(letters) for _ in range(rng.randint(3, 8)))])
    for _ in range(5_000):
        w = [rng.choice(letters) for _ in range(rng.randint(3, 8))]
        for i in rng.sample(range(len(w)), rng.randint(0, 2)):
            w[i] = "."
        ops.append("search")
        args.append(["".join(w)])
    return (ops, args)
