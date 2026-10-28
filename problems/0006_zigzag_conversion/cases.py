METHOD = "convert"

CASES = [
    dict(args=("PAYPALISHIRING", 3), expected="PAHNAPLSIIGYIR"),
    dict(args=("PAYPALISHIRING", 4), expected="PINALSIGYAHRPI"),
    dict(args=("A", 1), expected="A"),
    dict(args=("AB", 1), expected="AB"),
    dict(args=("ABCD", 2), expected="ACBD"),
    dict(args=("ABC", 5), expected="ABC"),
]
