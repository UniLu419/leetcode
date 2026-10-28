import random
import string

METHOD = "lengthOfLastWord"

CASES = [
    dict(args=("Hello World",), expected=5),
    dict(args=("   fly me   to   the moon  ",), expected=4),
    dict(args=("luffy is still joyboy",), expected=6),
    dict(args=("a",), expected=1),
    dict(args=("a   ",), expected=1),
    dict(args=("   day",), expected=3),
]


def bench():
    rng = random.Random(0)
    words = ["".join(rng.choices(string.ascii_letters, k=rng.randint(1, 10))) for _ in range(2_000)]
    return ((" ".join(words) + " " * 10)[:10_000],)
