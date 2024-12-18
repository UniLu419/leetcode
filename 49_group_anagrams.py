from typing import List
from timing_dec import timing


class Solution:
    # 用纯hash可以实现但是太慢了因为hash_map不能hash
    @timing
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

    @timing
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        hash_map = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in hash_map:
                hash_map[key].append(s)
            else:
                hash_map[key] = [s]
        return [value for value in hash_map.values()]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
                case 2:
                    # sample 2
                    strs = [""]
                case 3:
                    # sample 3
                    strs = ["a"]
                case _:
                    break
            print(f"ans = {solution.groupAnagrams(strs)}")
            print(f"ans = {solution.groupAnagrams2(strs)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
