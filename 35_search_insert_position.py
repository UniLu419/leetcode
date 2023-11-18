from typing import List
from utils import string_to_int_list


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while not left > right:
            # single left
            if left == right:
                if nums[left] < target:
                    return left + 1
                else:
                    return left
            # double left
            if right == left + 1:
                if nums[left] >= target:
                    return left
                else:
                    if nums[right] >= target:
                        return right
                    else:
                        return right + 1

            mid = (right - left) // 2 + left
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            s = input("Please enter a list of int: ")
            i = input("Please enter the int to insert: ")
            print(f"ans = {solution.searchInsert(string_to_int_list(s),int(i))}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
