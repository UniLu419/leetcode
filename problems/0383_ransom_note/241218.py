class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map_r = {}
        hash_map_m = {}
        for j in magazine:
            if j in hash_map_m:
                hash_map_m[j] += 1
            else:
                hash_map_m[j] = 1
        for i in ransomNote:
            if i not in hash_map_m:
                return False

            if i in hash_map_r:
                hash_map_r[i] += 1
            else:
                hash_map_r[i] = 1

            if hash_map_m[i] < hash_map_r[i]:
                return False
        return True
