class Solution:
    # hash完后统一判断快一点
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hash_map_r = {}
        hash_map_m = {}
        for j in magazine:
            if j in hash_map_m:
                hash_map_m[j] += 1
            else:
                hash_map_m[j] = 1
        for i in ransomNote:
            if i in hash_map_r:
                hash_map_r[i] += 1
            else:
                hash_map_r[i] = 1

        for key in hash_map_r.keys():
            if key not in hash_map_m or hash_map_m[key] < hash_map_r[key]:
                return False
        return True
