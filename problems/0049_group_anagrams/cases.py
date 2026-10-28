import random
import string

METHOD = "groupAnagrams"
UNORDERED = True

CASES = [
    dict(args=(["eat", "tea", "tan", "ate", "nat", "bat"],), expected=[["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
    dict(args=([""],), expected=[[""]]),
    dict(args=(["a"],), expected=[["a"]]),
    dict(args=(["", ""],), expected=[["", ""]]),
    dict(args=(["ab", "ba", "aab", "abb"],), expected=[["ab", "ba"], ["aab"], ["abb"]]),
]


def bench():
    rng = random.Random(0)
    return (["".join(rng.choices(string.ascii_lowercase, k=rng.randint(1, 100))) for _ in range(10_000)],)
