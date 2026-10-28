from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hash_map = {}
        for i, num in enumerate(nums):
            if num in hash_map:
                if i - hash_map[num][len(hash_map[num]) - 1] <= k:
                    return True
                hash_map[num].append(i)
            else:
                hash_map[num] = [i]

        return False
