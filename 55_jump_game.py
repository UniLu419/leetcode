from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        pass


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
