from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hash_map = {}
        calculated = [False for _ in nums]
        for i, num in enumerate(nums):
            hash_map[num] = i

        for i, num in enumerate(nums):
            if calculated[i]:
                continue
            target = num + 1
            temp = 1
            while target in hash_map:
                calculated[hash_map[target]] = True
                temp += 1
                target += 1
            target = num - 1
            while target in hash_map:
                calculated[hash_map[target]] = True
                temp += 1
                target -= 1
            if temp > longest:
                longest = temp
        return longest
