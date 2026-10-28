import random
import string

METHOD = "isAnagram"

CASES = [
    dict(args=("anagram", "nagaram"), expected=True),
    dict(args=("rat", "car"), expected=False),
    dict(args=("a", "a"), expected=True),
    dict(args=("a", "ab"), expected=False),
    dict(args=("aacc", "ccac"), expected=False),
    dict(args=("ab", "ba"), expected=True),
]


def bench():
    rng = random.Random(0)
    s = rng.choices(string.ascii_lowercase, k=50_000)
    t = s[:]
    rng.shuffle(t)
    return ("".join(s), "".join(t))
