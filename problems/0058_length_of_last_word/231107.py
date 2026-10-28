class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = s.split()[-1]
        return len(ans)
