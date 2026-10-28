import random

METHOD = "calculate"

CASES = [
    dict(args=("1 + 1",), expected=2),
    dict(args=(" 2-1 + 2 ",), expected=3),
    dict(args=("(1+(4+5+2)-3)+(6+8)",), expected=23),
    dict(args=("1-(     -2)",), expected=3),
    dict(args=("-(2+3)",), expected=-5),
    dict(args=("- (3 + (4 + 5))",), expected=-12),
    dict(args=("2147483647",), expected=2147483647),
    dict(args=("10-(2-(3-4))",), expected=7),
]


def bench():
    rng = random.Random(0)
    parts, depth = ["1"], 0
    while len(parts) < 55_000:
        op = rng.choice("+-")
        r = rng.random()
        if r < 0.2 and depth < 50:
            parts.append(op + "(" + str(rng.randint(0, 1000)))
            depth += 1
        elif r < 0.4 and depth > 0:
            parts.append(")")
            depth -= 1
        else:
            parts.append(op + str(rng.randint(0, 1000)))
    parts.append(")" * depth)
    return (" ".join(parts),)
