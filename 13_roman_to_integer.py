from typing import List
from timing_dec import timing


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "III"
                case 2:
                    # sample 2
                    s = "LVIII"
                case 3:
                    # sample 3
                    s = "MCMXCIV"
                case _:
                    break
            print(f"ans = {solution.romanToInt(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
