class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n = len(s)
        if len(t) != n:
            return False
        hash_map1 = {}
        hash_map2 = {}  # 注意这里要求不同字母不可以映射到同一个字母上，所以需要双向hash
        for i, j in zip(s, t):
            if i not in hash_map1:
                if j in hash_map2:
                    return False
                hash_map1[i] = j
                hash_map2[j] = i
            elif hash_map1[i] != j:
                return False
        return True
