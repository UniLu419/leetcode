import random

METHOD = "evalRPN"

CASES = [
    dict(args=(["2", "1", "+", "3", "*"],), expected=9),
    dict(args=(["4", "13", "5", "/", "+"],), expected=6),
    dict(args=(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"],), expected=22),
    dict(args=(["18"],), expected=18),
    dict(args=(["-7", "2", "/"],), expected=-3),
    dict(args=(["3", "-4", "*", "5", "-"],), expected=-17),
]


def bench():
    rng = random.Random(0)
    tokens = ["1"]
    while len(tokens) < 9_999:
        tokens += [str(rng.randint(-200, 200)), rng.choice("+-")]
    return (tokens,)
