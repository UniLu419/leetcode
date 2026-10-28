class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, n, m = 0, 0, len(s), len(t)
        while i < n and j < m:
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == n
