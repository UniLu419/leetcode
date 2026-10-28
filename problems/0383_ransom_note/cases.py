import random
import string

METHOD = "canConstruct"

CASES = [
    dict(args=("a", "b"), expected=False),
    dict(args=("aa", "ab"), expected=False),
    dict(args=("aa", "aab"), expected=True),
    dict(args=("a", "a"), expected=True),
    dict(args=("abc", "cba"), expected=True),
    dict(args=("aab", "baa"), expected=True),
    dict(args=("ab", "aaaa"), expected=False),
]


def bench():
    rng = random.Random(0)
    magazine = "".join(rng.choices(string.ascii_lowercase, k=100_000))
    ransom = "".join(rng.sample(magazine, 100_000))
    return (ransom, magazine)
