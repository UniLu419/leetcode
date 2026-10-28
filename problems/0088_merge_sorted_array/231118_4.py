from typing import List


class Solution:
    # 倒序双指针慢
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = m - 1
        index2 = n - 1
        index = m + n - 1
        while index >= 0:
            if index1 >= 0 and index2 >= 0:
                if nums1[index1] > nums2[index2]:
                    nums1[index] = nums1[index1]
                    index1 -= 1
                else:
                    nums1[index] = nums2[index2]
                    index2 -= 1
            elif index1 >= 0:
                nums1[index] = nums1[index1]
                index1 -= 1
            elif index2 >= 0:
                nums1[index] = nums2[index2]
                index2 -= 1
            index -= 1
