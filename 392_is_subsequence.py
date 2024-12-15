from typing import List
from timing_dec import timing


class Solution:
    @timing
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, n, m = 0, 0, len(s), len(t)
        while i < n and j < m:
            if t[j] == s[i]:
                i += 1
            j += 1
        return i == n


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    s = "abc"
                    t = "ahbgdc"
                case 2:
                    # sample 2
                    s = "axc"
                    t = "ahbgdc"
                case _:
                    break
            print(f"ans = {solution.isSubsequence(s,t)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
