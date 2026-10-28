class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        temp = x
        reversed = 0
        while temp > 0:
            tail = temp % 10
            reversed = reversed * 10 + tail
            temp = temp // 10
        return reversed == x
