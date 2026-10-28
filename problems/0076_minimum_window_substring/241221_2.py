from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:  # 不超时
        l, r = 0, -1
        n = len(s)
        c = Counter(t)
        cur_c = Counter()
        ans = ""
        # 维护current hash
        while l < n and r < n:
            current = s[l : r + 1]
            complete = True
            for key in c.keys():
                if cur_c[key] < c[key]:
                    complete = False
                    break
            if complete:
                if ans == "" or len(ans) > len(current):
                    ans = current
                cur_c[s[l]] -= 1
                l += 1
            else:
                r += 1
                if r < n:
                    cur_c[s[r]] += 1
        return ans
