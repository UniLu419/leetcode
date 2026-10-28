from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                hash_map[num].append(i)
            else:
                hash_map[num] = [i]
        for value in hash_map.values():
            n = len(value)
            if n > 1:
                for j in range(n - 1):
                    if value[j + 1] - value[j] <= k:
                        return True
        return False
