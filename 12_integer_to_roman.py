from typing import List
from timing_dec import timing


class Solution:
    @timing
    def intToRoman(self, num: int) -> str:
        match_table = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }
        divisors = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        s = ""
        for divisor in divisors:
            quotient, num = divmod(num, divisor)
            for i in range(quotient):
                s += match_table[divisor]
        return s

    @timing
    def intToRoman2(self, num: int) -> str:
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    num = 3749
                case 2:
                    # sample 2
                    num = 58
                case 3:
                    # sample 3
                    num = 1994
                case _:
                    break
            print(f"ans = {solution.intToRoman(num)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()


# 元组list比list+dict高效
