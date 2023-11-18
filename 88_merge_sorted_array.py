from typing import List
from utils import string_to_int_list


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


class Solution2:
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


def main():
    # Your main code goes here
    solution = Solution2()
    while True:
        try:
            nums1 = string_to_int_list(input("nums1: "))
            m = int(input("m: "))
            nums2 = string_to_int_list(input("nums2: "))
            n = int(input("n: "))
            solution.merge(nums1, m, nums2, n)
            print(f"nums1 = {nums1}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
