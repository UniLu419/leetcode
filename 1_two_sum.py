from typing import List
from timing_dec import timing


class Solution:
    @timing
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(nums):
            if num not in hash_map:
                hash_map[num] = [i]
            else:
                hash_map[num].append(i)
        for i, num in enumerate(nums):
            temp = target - num
            if temp == num:
                if len(hash_map[temp]) == 2:  # 这句不能和上面的条件合并
                    return hash_map[temp]
            elif temp in hash_map:
                return [hash_map[num][0], hash_map[temp][0]]
        return []


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [2, 7, 11, 15]
                    target = 9
                case 2:
                    # sample 2
                    nums = [3, 2, 4]
                    target = 6
                case 3:
                    # sample 3
                    nums = [3, 3]
                    target = 6
                case _:
                    break
            print(f"ans = {solution.twoSum(nums,target)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
