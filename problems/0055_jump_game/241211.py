from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = [False] * n
        ans[0] = True
        for i in range(n):
            if ans[i]:
                for j in range(nums[i]):
                    index = i + j + 1
                    if index < n - 1:
                        ans[index] = True
                    elif index == n - 1:
                        return True
        return ans[n - 1]
