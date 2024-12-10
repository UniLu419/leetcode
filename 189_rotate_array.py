from typing import List

from timing_dec import timing


class Solution:
    @timing
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        for i in range(k):
            temp = nums.pop()
            nums.insert(0, temp)

    @timing
    def rotate2(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [1, 2, 3, 4, 5, 6, 7]
                    k = 3
                case 2:
                    # sample 2
                    nums = [-1, -100, 3, 99]
                    k = 2
                case _:
                    break
            solution.rotate(nums, k)
            solution.rotate2(nums, k)
            print(f"ans = {nums}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
