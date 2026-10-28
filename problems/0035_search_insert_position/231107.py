from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while not left > right:
            # single left
            if left == right:
                if nums[left] < target:
                    return left + 1
                else:
                    return left
            # double left
            if right == left + 1:
                if nums[left] >= target:
                    return left
                else:
                    if nums[right] >= target:
                        return right
                    else:
                        return right + 1

            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
