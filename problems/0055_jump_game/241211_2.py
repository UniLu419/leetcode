from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max = 0
        for i, jump in enumerate(nums):
            destination = i + jump
            if max >= i and destination > max:
                max = destination
        return max >= len(nums) - 1
