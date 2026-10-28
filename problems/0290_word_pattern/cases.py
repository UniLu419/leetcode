METHOD = "wordPattern"

CASES = [
    dict(args=("abba", "dog cat cat dog"), expected=True),
    dict(args=("abba", "dog cat cat fish"), expected=False),
    dict(args=("aaaa", "dog cat cat dog"), expected=False),
    dict(args=("abba", "dog dog dog dog"), expected=False),
    dict(args=("a", "dog"), expected=True),
    dict(args=("aaa", "aa aa aa aa"), expected=False),
    dict(args=("ab", "dog dog"), expected=False),
]
