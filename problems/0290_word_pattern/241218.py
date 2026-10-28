class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        hash_map1 = {}
        hash_map2 = {}
        s_list = s.split()
        if len(s_list) != len(pattern):
            return False
        for i, j in zip(s_list, pattern):
            if i not in hash_map1:
                if j in hash_map2:
                    return False
                hash_map1[i] = j
                hash_map2[j] = i
            elif hash_map1[i] != j:
                return False
        return True
