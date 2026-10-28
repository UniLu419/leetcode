import random
import string

METHOD = "minWindow"

CASES = [
    dict(args=("ADOBECODEBANC", "ABC"), expected="BANC"),
    dict(args=("a", "a"), expected="a"),
    dict(args=("a", "aa"), expected=""),
    dict(args=("ab", "b"), expected="b"),
    dict(args=("aa", "aa"), expected="aa"),
    dict(args=("bba", "ab"), expected="ba"),
    dict(args=("abc", "d"), expected=""),
]


def bench():
    rng = random.Random(0)
    s = "".join(rng.choices(string.ascii_letters, k=100_000))
    t = "".join(rng.choices(string.ascii_letters, k=40))
    return (s, t)
