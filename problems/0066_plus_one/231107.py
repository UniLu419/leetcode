from typing import List


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
