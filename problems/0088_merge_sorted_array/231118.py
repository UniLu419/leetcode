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

        while index_n < n:
            if index_m >= m:
                nums1[index_m + index_n] = nums2[index_n]
                index_n += 1
                continue
            if nums1[index_m + index_n] >= nums2[index_n]:
                index = m + n - 2
                while index >= index_m + index_n:
                    nums1[index + 1] = nums1[index]
                    index -= 1
                nums1[index_m + index_n] = nums2[index_n]
                index_n += 1
            else:
                index_m += 1
