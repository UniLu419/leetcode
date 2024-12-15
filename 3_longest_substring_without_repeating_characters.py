from typing import List
from timing_dec import timing


class Solution:
    @timing
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map: dict[str, int] = {}
        max_len = 0
        n = len(s)
        l, r = 0, -1
        while l < n and r < n:
            length = r - l + 1
            print(f"l: {l} r: {r} length: {length}")
            print(s[l : r + 1])
            if length > max_len:
                max_len = length

            r += 1
            if r < n:
                # 和之前239求固定长度子序列最大值那道题一样，需要注意下标是否在窗口内
                if s[r] in hash_map and hash_map[s[r]] >= l:
                    l = hash_map[s[r]] + 1
                    hash_map[s[r]] = r
                else:
                    hash_map[s[r]] = r
        return max_len


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "abcabcbb"
                case 2:
                    # sample 2
                    s = "bbbbb"
                case 3:
                    # sample 3
                    s = "pwwkew"
                case 4:
                    # sample 4
                    s = "abba"
                case _:
                    break
            print(f"ans = {solution.lengthOfLongestSubstring(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
