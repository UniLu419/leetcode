from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_list = [1] * n
        suffix_list = [1] * n
        for i in range(1, len(nums)):
            prefix_list[i] = prefix_list[i - 1] * nums[i - 1]
            suffix_list[n - 1 - i] = suffix_list[n - i] * nums[n - i]

        ans = [pre * suf for pre, suf in zip(prefix_list, suffix_list)]
        return ans
