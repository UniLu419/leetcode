import random
import string

METHOD = "isIsomorphic"

CASES = [
    dict(args=("egg", "add"), expected=True),
    dict(args=("foo", "bar"), expected=False),
    dict(args=("paper", "title"), expected=True),
    dict(args=("badc", "baba"), expected=False),
    dict(args=("a", "a"), expected=True),
    dict(args=("ab", "aa"), expected=False),
    dict(args=("13", "42"), expected=True),
]


def bench():
    rng = random.Random(0)
    letters = string.ascii_lowercase
    mapping = dict(zip(letters, rng.sample(letters, len(letters))))
    s = "".join(rng.choices(letters, k=50_000))
    return (s, "".join(mapping[c] for c in s))
