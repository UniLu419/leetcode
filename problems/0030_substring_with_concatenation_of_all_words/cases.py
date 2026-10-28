import random

METHOD = "findSubstring"
UNORDERED = True

CASES = [
    dict(args=("barfoothefoobarman", ["foo", "bar"]), expected=[0, 9]),
    dict(args=("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]), expected=[]),
    dict(args=("barfoofoobarthefoobarman", ["bar", "foo", "the"]), expected=[6, 9, 12]),
    dict(args=("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]), expected=[8]),
    dict(
        args=("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"]),
        expected=[13],
    ),
    dict(args=("aaaaaaaaaaaaaa", ["aa", "aa"]), expected=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    dict(args=("abaabaaa", ["ba", "ab"]), expected=[1]),
    dict(args=("a", ["a"]), expected=[0]),
    dict(args=("ab", ["abc"]), expected=[]),
]


def bench():
    rng = random.Random(0)
    s = "".join(rng.choice("ab") for _ in range(10_000))
    return (s, ["ab", "ba", "ab", "aa", "bb"])
