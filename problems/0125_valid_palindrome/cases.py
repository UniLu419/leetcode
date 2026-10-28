import random
import string

METHOD = "isPalindrome"

CASES = [
    dict(args=("A man, a plan, a canal: Panama",), expected=True),
    dict(args=("race a car",), expected=False),
    dict(args=(" ",), expected=True),
    dict(args=("0P",), expected=False),
    dict(args=("a.",), expected=True),
    dict(args=("Ab_a",), expected=True),
]


def bench():
    rng = random.Random(0)
    half = "".join(rng.choices(string.ascii_letters + string.digits + " ,.:!", k=100_000))
    return (half + half[::-1],)
