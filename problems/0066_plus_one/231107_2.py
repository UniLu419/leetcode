from typing import List


class Solution:
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
