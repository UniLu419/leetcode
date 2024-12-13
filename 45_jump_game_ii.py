from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        ans = [-1] * n
        ans[0] = 0
        for i in range(n):
            if ans[i] != -1:
                for j in range(nums[i]):
                    index = i + j + 1
                    if index < n - 1:
                        ans[index] = (
                            min(ans[index], ans[i] + 1)
                            if ans[index] != -1
                            else ans[i] + 1
                        )
                    elif index == n - 1:
                        return ans[i] + 1
        return ans[n - 1]

    def jump2(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        end = 0
        step = 0
        for i in range(n - 1):
            max_len = max(max_len, nums[i] + i)
            if i == end:
                end = max_len
                step += 1
        return step


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
                    nums = [2, 3, 0, 1, 4]
                case _:
                    break
            print(f"ans = {solution.jump(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
