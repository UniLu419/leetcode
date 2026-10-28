class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        parsed_s = [char for char in s if char.isalnum()]
        l, r = 0, len(parsed_s) - 1
        while l < r:
            if parsed_s[l] != parsed_s[r]:
                return False
            l += 1
            r -= 1
        return True
