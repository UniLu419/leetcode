from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if val != num:
                nums[i] = num
                i += 1
        return i
