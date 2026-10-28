METHOD = "longestCommonPrefix"

CASES = [
    dict(args=(["flower", "flow", "flight"],), expected="fl"),
    dict(args=(["dog", "racecar", "car"],), expected=""),
    dict(args=([""],), expected=""),
    dict(args=(["a"],), expected="a"),
    dict(args=(["ab", "a"],), expected="a"),
    dict(args=(["", "b"],), expected=""),
    dict(args=(["abc", "abc", "abc"],), expected="abc"),
]
