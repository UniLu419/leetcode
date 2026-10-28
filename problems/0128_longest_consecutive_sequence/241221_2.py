from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        nums = sorted(nums)
        cur_max, ans_max = 1, 0
        for i in range(1, n):
            pre = nums[i - 1]
            if pre == nums[i]:
                continue
            elif pre + 1 == nums[i]:
                cur_max += 1
            else:
                if cur_max > ans_max:
                    ans_max = cur_max
                cur_max = 1
        if cur_max > ans_max:  # 不要忘记最后一个
            ans_max = cur_max
        return ans_max
