METHOD = "longestPalindrome"

CASES = [
    dict(args=("babad",), expected="bab"),
    dict(args=("cbbd",), expected="bb"),
    dict(args=("a",), expected="a"),
    dict(args=("ac",), expected="a"),
    dict(args=("aaaa",), expected="aaaa"),
    dict(args=("forgeeksskeegfor",), expected="geeksskeeg"),
]


def check(output, expected, args):
    """Any longest palindromic substring is accepted ("babad" -> "bab" or "aba")."""
    s = args[0]
    return isinstance(output, str) and len(output) == len(expected) and output == output[::-1] and output in s
