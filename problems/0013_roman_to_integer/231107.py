class Solution:
    def romanToInt(self, s: str) -> int:
        match_table = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }
        index = 0
        n = len(s)
        total = 0
        while index < n:
            if index + 1 < n:
                double_s = s[index] + s[index + 1]
                if double_s in match_table:
                    total += match_table[double_s]
                    index += 2
                else:
                    total += match_table[s[index]]
                    index += 1
            else:
                total += match_table[s[index]]
                index += 1
        return total
