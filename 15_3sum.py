from typing import List
from timing_dec import timing


class Solution:
    @timing
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        i = 0
        ans = []
        while i < n:
            ni = nums[i]
            target = -ni
            l, r = i + 1, n - 1
            while l < r:
                nl, nr = nums[l], nums[r]
                ns = nl + nr
                if ns < target:
                    while l < r and nums[l] == nl:
                        l += 1
                elif ns > target:
                    while l < r and nums[r] == nr:
                        r -= 1
                else:
                    ans.append([ni, nl, nr])
                    while l < r and nums[l] == nl:
                        l += 1
                    while l < r and nums[r] == nr:
                        r -= 1
            while i < n and ni == nums[i]:
                i += 1
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
                    nums = [-1, 0, 1, 2, -1, -4]
                case 2:
                    # sample 2
                    nums = [0, 1, 1]
                case 3:
                    # sample 3
                    nums = [0, 0, 0]
                case _:
                    break
            print(f"ans = {solution.threeSum(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
