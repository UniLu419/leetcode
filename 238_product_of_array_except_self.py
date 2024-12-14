import enum
from typing import List
from timing_dec import timing


class Solution:
    @timing
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_list = [1] * n
        suffix_list = [1] * n
        for i in range(1, len(nums)):
            prefix_list[i] = prefix_list[i - 1] * nums[i - 1]
            suffix_list[n - 1 - i] = suffix_list[n - i] * nums[n - i]

        ans = [pre * suf for pre, suf in zip(prefix_list, suffix_list)]
        return ans


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [1, 2, 3, 4]
                case 2:
                    # sample 2
                    nums = [-1, 1, 0, -3, 3]
                case _:
                    break
            print(f"ans = {solution.productExceptSelf(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
