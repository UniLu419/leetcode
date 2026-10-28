METHOD = "strStr"

CASES = [
    dict(args=("sadbutsad", "sad"), expected=0),
    dict(args=("leetcode", "leeto"), expected=-1),
    dict(args=("a", "a"), expected=0),
    dict(args=("abc", "c"), expected=2),
    dict(args=("aaa", "aaaa"), expected=-1),
    dict(args=("mississippi", "issip"), expected=4),
]


def bench():
    return ("a" * 10_000, "a" * 5_000 + "b")
