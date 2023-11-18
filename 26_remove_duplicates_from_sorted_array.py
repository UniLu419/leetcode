from typing import List
from utils import string_to_int_list


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        i = 1
        while i < len(nums):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                i += 1
        print(f"nums = {nums}")
        return len(nums)


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a list of int: ")
            print(f"k = {solution.removeDuplicates(string_to_int_list(s))}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
