from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        ans = [False] * n
        ans[0] = True
        for i in range(n):
            if ans[i]:
                for j in range(nums[i]):
                    index = i + j + 1
                    if index < n - 1:
                        ans[index] = True
                    elif index == n - 1:
                        return True
        return ans[n - 1]

    def canJump2(self, nums: List[int]) -> bool:
        max = 0
        for i, jump in enumerate(nums):
            destination = i + jump
            if max >= i and destination > max:
                max = destination
        return max >= len(nums) - 1


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [2, 3, 1, 1, 4]
                case 2:
                    # sample 2
                    nums = [3, 2, 1, 0, 4]
                case _:
                    break
            print(f"ans = {solution.canJump(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
