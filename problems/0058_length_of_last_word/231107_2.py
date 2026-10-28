class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        ans = 0
        start = False
        for i in range(n):
            if s[n - 1 - i] != " ":
                start = True
                ans += 1
            elif start:
                break
        return ans
