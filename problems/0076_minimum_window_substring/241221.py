from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:  # 超时
        l, r = 0, -1
        n = len(s)
        c = Counter(t)
        ans = ""
        # 滑动之后取hash比较大小
        while l < n and r < n:
            current = s[l : r + 1]
            cur_c = Counter(current)
            complete = True
            for key in c.keys():
                if cur_c[key] < c[key]:
                    complete = False
                    break
            if complete:
                if ans == "" or len(ans) > len(current):
                    ans = current
                l += 1
            else:
                r += 1
        return ans
