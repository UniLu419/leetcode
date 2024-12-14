from typing import List
from timing_dec import timing


class Solution:
    @timing
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def get_prefix(s1: str, s2: str) -> str:
            n = min(len(s1), len(s2))
            t = ""
            for i in range(n):
                if s1[i] == s2[i]:
                    t += s1[i]
                else:
                    break
            return t

        prefix = strs[0]
        for i in range(1, len(strs)):
            prefix = get_prefix(prefix, strs[i])
            if len(prefix) == 0:
                break
        return prefix

    @timing
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        l = min([len(s) for s in strs])
        n = len(strs)
        prefix = ""
        for i in range(l):
            flag = True
            for j in range(n - 1):
                if strs[j][i] != strs[j + 1][i]:
                    flag = False
                    break
            if flag:
                prefix += strs[0][i]
            else:
                break
        return prefix


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    strs = ["flower", "flow", "flight"]
                case 2:
                    # sample 2
                    strs = ["dog", "racecar", "car"]
                case _:
                    break
            print(f"ans = {solution.longestCommonPrefix(strs)}")
            print(f"ans = {solution.longestCommonPrefix2(strs)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
