METHOD = "intToRoman"

CASES = [
    dict(args=(3749,), expected="MMMDCCXLIX"),
    dict(args=(58,), expected="LVIII"),
    dict(args=(1994,), expected="MCMXCIV"),
    dict(args=(1,), expected="I"),
    dict(args=(4,), expected="IV"),
    dict(args=(400,), expected="CD"),
    dict(args=(3999,), expected="MMMCMXCIX"),
]
