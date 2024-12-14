from typing import List
from timing_dec import timing


class Solution:
    @timing
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)

    @timing
    def strStr1(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        for i in range(n - m + 1):  # 注意这里的边界需要+1
            if haystack[i : i + m] == needle:
                return i
        return -1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    haystack = "sadbutsad"
                    needle = "sad"
                case 2:
                    # sample 2
                    haystack = "leetcode"
                    needle = "leeto"
                case 3:
                    # sample 3
                    haystack = "abc"
                    needle = "c"
                case _:
                    break
            print(f"ans = {solution.strStr(haystack,needle)}")
            print(f"ans = {solution.strStr1(haystack,needle)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
