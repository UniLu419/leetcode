from typing import List
from timing_dec import timing


class Solution:
    @timing
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

    @timing
    def merge2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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

    # 新数组快
    @timing
    def merge3(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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

    # 倒序双指针慢
    @timing
    def merge4(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums1 = [1, 2, 3, 0, 0, 0]
                    m = 3
                    nums2 = [2, 5, 6]
                    n = 3
                case 2:
                    # sample 2
                    nums1 = [1]
                    m = 1
                    nums2 = []
                    n = 0
                case 3:
                    # sample 3
                    nums1 = [0]
                    m = 0
                    nums2 = [1]
                    n = 1
                case 4:
                    # sample 4
                    nums1 = [2, 0]
                    m = 1
                    nums2 = [1]
                    n = 1
                case _:
                    break
            # 无返回值的题不能同时print
            # print(f"ans = {solution.merge(nums1,m,nums2,n)}")
            # print(f"ans = {solution.merge2(nums1,m,nums2,n)}")
            # print(f"ans = {solution.merge3(nums1,m,nums2,n)}")
            print(f"ans = {solution.merge4(nums1,m,nums2,n)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
