import random
import string

METHOD = "isSubsequence"

CASES = [
    dict(args=("abc", "ahbgdc"), expected=True),
    dict(args=("axc", "ahbgdc"), expected=False),
    dict(args=("", "ahbgdc"), expected=True),
    dict(args=("", ""), expected=True),
    dict(args=("a", ""), expected=False),
    dict(args=("aaa", "aa"), expected=False),
    dict(args=("ab", "ba"), expected=False),
]


def bench():
    rng = random.Random(0)
    t = "".join(rng.choices(string.ascii_lowercase[:25], k=10_000))
    s = t[::100][:99] + "z"
    return (s, t)
