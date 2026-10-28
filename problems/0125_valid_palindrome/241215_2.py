class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        parsed_s = [char for char in s if char.isalnum()]
        return parsed_s == parsed_s[::-1]
