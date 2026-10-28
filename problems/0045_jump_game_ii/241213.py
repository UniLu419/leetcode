from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [-1] * n
        ans[0] = 0
        for i in range(n):
            if ans[i] != -1:
                for j in range(nums[i]):
                    index = i + j + 1
                    if index < n - 1:
                        ans[index] = (
                            min(ans[index], ans[i] + 1)
                            if ans[index] != -1
                            else ans[i] + 1
                        )
                    elif index == n - 1:
                        return ans[i] + 1
        return ans[n - 1]
