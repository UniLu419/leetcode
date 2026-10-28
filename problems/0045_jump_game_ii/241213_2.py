from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        end = 0
        step = 0
        for i in range(n - 1):
            max_len = max(max_len, nums[i] + i)
            if i == end:
                end = max_len
                step += 1
        return step
