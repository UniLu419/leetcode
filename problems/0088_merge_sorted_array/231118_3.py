from typing import List


class Solution:
    # 新数组快
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        merged_nums = []
        index_1 = 0
        index_2 = 0
        while index_1 < m and index_2 < n:
            if nums1[index_1] > nums2[index_2]:
                merged_nums.append(nums2[index_2])
                index_2 += 1
            else:
                merged_nums.append(nums1[index_1])
                index_1 += 1
        for i in range(index_1, m):
            merged_nums.append(nums1[i])
        for j in range(index_2, n):
            merged_nums.append(nums2[j])
        for q in range(len(nums1)):
            nums1[q] = merged_nums[q]
