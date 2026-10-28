class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False
        hash_map_s = {}
        hash_map_t = {}
        for i in range(n):
            if s[i] in hash_map_s:
                hash_map_s[s[i]] += 1  # 注意下标不要写错！
            else:
                hash_map_s[s[i]] = 1
            if t[i] in hash_map_t:
                hash_map_t[t[i]] += 1
            else:
                hash_map_t[t[i]] = 1
        for key in hash_map_s.keys():
            if key not in hash_map_t or hash_map_s[key] != hash_map_t[key]:
                return False

        return True
