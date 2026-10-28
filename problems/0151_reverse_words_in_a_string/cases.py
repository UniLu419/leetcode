import random
import string

METHOD = "reverseWords"

CASES = [
    dict(args=("the sky is blue",), expected="blue is sky the"),
    dict(args=("  hello world  ",), expected="world hello"),
    dict(args=("a good   example",), expected="example good a"),
    dict(args=("a",), expected="a"),
    dict(args=("   a   ",), expected="a"),
    dict(args=("  Bob    Loves  Alice   ",), expected="Alice Loves Bob"),
]


def bench():
    rng = random.Random(0)
    parts = []
    while sum(map(len, parts)) < 9_900:
        parts.append(" " * rng.randint(1, 3) + "".join(rng.choices(string.ascii_letters + string.digits, k=rng.randint(1, 8))))
    return ("".join(parts),)
