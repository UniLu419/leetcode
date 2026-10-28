import random

METHOD = "addBinary"

CASES = [
    dict(args=("11", "1"), expected="100"),
    dict(args=("1010", "1011"), expected="10101"),
    dict(args=("0", "0"), expected="0"),
    dict(args=("1", "111"), expected="1000"),
    dict(args=("1111", "1111"), expected="11110"),
    dict(args=("100", "0"), expected="100"),
]


def bench():
    rng = random.Random(0)
    a = "1" + "".join(rng.choices("01", k=9_999))
    b = "1" + "".join(rng.choices("01", k=9_999))
    return (a, b)
