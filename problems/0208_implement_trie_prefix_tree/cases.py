import random

CLASS = "Trie"

CASES = [
    dict(ops=['Trie', 'insert', 'search', 'search', 'startsWith', 'insert', 'search'], args=[[], ['apple'], ['apple'], ['app'], ['app'], ['app'], ['app']], expected=[None, None, True, False, True, None, True]),
    # 空树查询；单字符；更长的前缀
    dict(ops=['Trie', 'search', 'startsWith', 'insert', 'search', 'startsWith', 'search', 'startsWith'], args=[[], ['a'], ['a'], ['a'], ['a'], ['a'], ['ab'], ['ab']], expected=[None, False, False, None, True, True, False, False]),
    # 前缀不是完整单词；整词也算自己的前缀；重复插入
    dict(ops=['Trie', 'insert', 'search', 'startsWith', 'startsWith', 'startsWith', 'insert', 'search', 'search'], args=[[], ['abc'], ['ab'], ['abc'], ['abcd'], ['b'], ['abc'], ['abc'], ['abcd']], expected=[None, None, False, True, False, False, None, True, False]),
]


def bench():
    rng = random.Random(0)

    def word():
        return "".join(rng.choice("abcde") for _ in range(rng.randint(1, 12)))

    ops, args = ["Trie"], [[]]
    for _ in range(10_000):
        ops.append("insert")
        args.append([word()])
    for _ in range(10_000):
        ops.append(rng.choice(["search", "startsWith"]))
        args.append([word()])
    return (ops, args)
