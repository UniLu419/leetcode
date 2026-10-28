from typing import List


class Solution:
    # 用纯hash可以实现但是太慢了因为hash_map不能hash
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        ans_indexes = []
        hash_maps = [self.create_hash_map(s) for s in strs]

        for i in range(n):
            finished = False
            for group in ans_indexes:
                if self.is_same(hash_maps[i], hash_maps[group[0]]):
                    group.append(i)
                    finished = True
            if not finished:
                ans_indexes.append([i])
        return [[strs[index] for index in group] for group in ans_indexes]

    def is_same(self, hash_map1: dict[str, int], hash_map2: dict[str, int]) -> bool:
        for key in hash_map1.keys():
            if key not in hash_map2 or hash_map1[key] != hash_map2[key]:
                return False
        for key in hash_map2.keys():
            if key not in hash_map1 or hash_map1[key] != hash_map2[key]:
                return False
        return True

    def create_hash_map(self, s: str) -> dict[str, int]:
        hash_map = {}
        for t in s:
            if t in hash_map:
                hash_map[t] += 1
            else:
                hash_map[t] = 1
        return hash_map
