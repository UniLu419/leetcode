from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dictionary: dict[int, int] = {}
        for num in nums:
            if num not in dictionary:
                dictionary[num] = 1
            else:
                dictionary[num] += 1
        max = None
        for key in dictionary.keys():
            if max is None:
                max = key
            if dictionary[key] > dictionary[max]:
                max = key
        return max


class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [3, 2, 3]
                case 2:
                    # sample 2
                    nums = [2, 2, 1, 1, 1, 2, 2]
                case _:
                    break
            print(f"ans = {solution.majorityElement(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
