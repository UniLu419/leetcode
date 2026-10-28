METHOD = "getShiftedString"

CASES = [
    dict(args=("abcde", 1, 2), expected="eabcd"),
    dict(args=("a", 3, 5), expected="a"),
    dict(args=("abcd", 5, 0), expected="bcda"),
    dict(args=("abcd", 0, 6), expected="cdab"),
    dict(args=("hello", 2, 2), expected="hello"),
]
