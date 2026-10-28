from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = [i]
            else:
                hash_map[num].append(i)
        for i, num in enumerate(nums):
            temp = target - num
            if temp == num:
                if len(hash_map[temp]) == 2:  # 这句不能和上面的条件合并
                    return hash_map[temp]
            elif temp in hash_map:
                return [hash_map[num][0], hash_map[temp][0]]
        return []
