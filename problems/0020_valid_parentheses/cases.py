import random

METHOD = "isValid"

CASES = [
    dict(args=("()",), expected=True),
    dict(args=("()[]{}",), expected=True),
    dict(args=("(]",), expected=False),
    dict(args=("([])",), expected=True),
    dict(args=("([)]",), expected=False),
    dict(args=("(",), expected=False),
    dict(args=("]",), expected=False),
    dict(args=("{[]}",), expected=True),
]


def bench():
    rng = random.Random(0)
    pairs = {"(": ")", "[": "]", "{": "}"}
    out, stack = [], []
    while len(out) + len(stack) < 10_000:
        if stack and (len(out) + 2 * len(stack) >= 10_000 or rng.random() < 0.5):
            out.append(pairs[stack.pop()])
        else:
            stack.append(rng.choice("([{"))
            out.append(stack[-1])
    out.extend(pairs[c] for c in reversed(stack))
    return ("".join(out),)
