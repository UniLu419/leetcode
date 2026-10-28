from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            ni = nums[i]
            target = -ni
            l, r = i + 1, n - 1
            while l < r:
                nl, nr = nums[l], nums[r]
                ns = nl + nr
                if ns < target:
                    while l < r and nums[l] == nl:
                        l += 1
                elif ns > target:
                    while l < r and nums[r] == nr:
                        r -= 1
                else:
                    ans.append([ni, nl, nr])
                    while l < r and nums[l] == nl:
                        l += 1
                    while l < r and nums[r] == nr:
                        r -= 1
            while i < n and ni == nums[i]:
                i += 1
        return ans
