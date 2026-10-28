from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
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
