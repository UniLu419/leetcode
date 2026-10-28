import random
import string

METHOD = "lengthOfLongestSubstring"

CASES = [
    dict(args=("abcabcbb",), expected=3),
    dict(args=("bbbbb",), expected=1),
    dict(args=("pwwkew",), expected=3),
    dict(args=("",), expected=0),
    dict(args=(" ",), expected=1),
    dict(args=("abba",), expected=2),
    dict(args=("dvdf",), expected=3),
]


def bench():
    rng = random.Random(0)
    return ("".join(rng.choices(string.ascii_letters + string.digits, k=50_000)),)
