from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, sum, n = 0, -1, 0, len(nums)
        min_length = n + 1
        while l < n and r < n:
            if sum >= target:
                length = r - l + 1
                if length < min_length:
                    min_length = length
                sum -= nums[l]  # 一定注意先减后挪
                l += 1
            else:
                r += 1
                if r < n:
                    sum += nums[r]

        return 0 if min_length == n + 1 else min_length
