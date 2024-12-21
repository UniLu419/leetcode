from typing import Counter, List
from timing_dec import timing


class Solution:
    @timing
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

    @timing
    def minWindow2(self, s: str, t: str) -> str:  # 不超时
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

    @timing
    def minWindow3(self, s: str, t: str) -> str:  # 不超时
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
            current = s[l : r + 1]
            if less == 0:
                if ans == "" or len(ans) > len(current):
                    ans = current
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

    @timing
    def minWindow4(self, s: str, t: str) -> str:  # 不超时
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "ADOBECODEBANC"
                    t = "ABC"
                case 2:
                    # sample 2
                    s = "a"
                    t = "a"
                case 3:
                    # sample 3
                    s = "a"
                    t = "aa"
                case _:
                    break
            print(f"ans = {solution.minWindow(s,t)}")
            print(f"ans = {solution.minWindow2(s,t)}")
            print(f"ans = {solution.minWindow3(s,t)}")
            print(f"ans = {solution.minWindow4(s,t)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
