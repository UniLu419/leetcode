from typing import List
from timing_dec import timing


class Solution:
    @timing
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r, sum, n = 0, -1, 0, len(nums)
        min_length = n + 1
        while l < n and r < n:
            print(nums[l : r + 1])
            print(f"l: {l} r: {r} sum: {sum}")
            if sum >= target:
                length = r - l + 1
                if length < min_length:
                    min_length = length
                sum -= nums[l]  # 一定注意先减后挪
                l += 1
            else:
                r += 1
                if r < n:
                    sum += nums[r]

        return 0 if min_length == n + 1 else min_length


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    target = 7
                    nums = [2, 3, 1, 2, 4, 3]
                case 2:
                    # sample 2
                    target = 4
                    nums = [1, 4, 4]
                case 3:
                    # sample 3
                    target = 11
                    nums = [1, 1, 1, 1, 1, 1, 1, 1]
                case 4:
                    # sample 4
                    target = 11
                    nums = [1, 2, 3, 4, 5]
                case _:
                    break
            print(f"ans = {solution.minSubArrayLen(target,nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
