from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        index_m = 0
        index_n = 0

        sum_nums = [0] * len(nums1)
        while index_m < m and index_n < n:
            if nums1[index_m] >= nums2[index_n]:
                sum_nums[index_n + index_m] = nums2[index_n]
                index_n += 1
            else:
                sum_nums[index_n + index_m] = nums1[index_m]
                index_m += 1
        while index_m < m:
            sum_nums[index_n + index_m] = nums1[index_m]
            index_m += 1
        while index_n < n:
            sum_nums[index_n + index_m] = nums2[index_n]
            index_n += 1
        for i in range(len(nums1)):
            nums1[i] = sum_nums[i]
