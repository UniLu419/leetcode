from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        k = 1
        for i in range(2, len(nums)):
            if nums[k - 1] != nums[i]:
                nums[k + 1] = nums[i]
                k += 1
        return k + 1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("s: ")
            print(f"ans = {solution.removeDuplicates(s)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
