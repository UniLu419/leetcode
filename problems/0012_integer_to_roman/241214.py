class Solution:
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
