from typing import List

from utils import string_to_int_list


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        quotient = 1
        while i >= 0:
            digits[i] += quotient
            if digits[i] == 10:
                digits[i] = 0
                quotient = 1
                i -= 1
            else:
                return digits
        if quotient == 1:
            digits.insert(0, 1)
            return digits


class Solution2:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        quotient = 1
        while i >= 0:
            current = digits[i]
            digits[i] = (current + quotient) % 10
            quotient = (current + quotient) // 10
            if quotient > 0:
                i -= 1
            else:
                return digits
        if i == -1 and quotient != 0:
            digits.append(digits[len(digits) - 1])
            for j in range(len(digits) - 1):
                digits[j + 1] = digits[j]
            digits[0] = quotient
            return digits


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a list of int: ")
            print(f"ans = {solution.plusOne(string_to_int_list(s))}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
