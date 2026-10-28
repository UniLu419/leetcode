class Solution:
    def intToRoman(self, num: int) -> str:
        # 注意打表不要打错
        roman_map = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I"),
        ]
        s = ""
        for value, symbol in roman_map:
            while num >= value:  # 这里注意等号
                s += symbol
                num -= value

        return s


# 元组list比list+dict高效
