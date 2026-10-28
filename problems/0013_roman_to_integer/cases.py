METHOD = "romanToInt"

CASES = [
    dict(args=("III",), expected=3),
    dict(args=("LVIII",), expected=58),
    dict(args=("MCMXCIV",), expected=1994),
    dict(args=("I",), expected=1),
    dict(args=("IV",), expected=4),
    dict(args=("XLIX",), expected=49),
    dict(args=("MMMCMXCIX",), expected=3999),
]
