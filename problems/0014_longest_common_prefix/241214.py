from typing import List


class Solution:
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
