from typing import List

from utils import string_to_int_list


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for num in nums:
            if val != num:
                nums[i] = num
                i += 1
        return i


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a list of int separated with single space: ")
            val = input("Please enter the integer that you want to delete: ")
            print(f"k = {solution.removeElement(string_to_int_list(s),int(val))}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
