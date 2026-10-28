from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:  # 不超时
        l, r = 0, -1
        n = len(s)
        less = 0
        c = Counter()
        ans = ""
        cur_c = Counter()
        # 维护less 和 hash
        for char in t:
            if char not in c:
                less += 1
                c[char] = 1
            else:
                c[char] += 1
        while l < n and r < n:
            if less == 0:
                # 直接计算下标长度
                if ans == "" or len(ans) > (r - l):
                    ans = s[l : r + 1]
                if cur_c[s[l]] == c[s[l]]:
                    less += 1
                cur_c[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < n:
                    cur_c[s[r]] += 1
                    if cur_c[s[r]] == c[s[r]]:
                        less -= 1
        return ans
