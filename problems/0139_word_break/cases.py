METHOD = "wordBreak"

CASES = [
    dict(args=('leetcode', ['leet', 'code'],), expected=True),
    dict(args=('applepenapple', ['apple', 'pen'],), expected=True),
    dict(args=('catsandog', ['cats', 'dog', 'sand', 'and', 'cat'],), expected=False),
    dict(args=('a', ['a']), expected=True),
    dict(args=('cars', ['car', 'ca', 'rs']), expected=True),
    dict(args=('aaaaaaa', ['aaaa', 'aaa']), expected=True),
    dict(args=('a' * 299 + 'b', ['a' * i for i in range(1, 11)]), expected=False),
]
