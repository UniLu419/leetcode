from typing import List
from timing_dec import timing


class Solution:
    @timing
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i, num in enumerate(numbers):
            if num in hash_map:
                hash_map[num].append(i + 1)
            else:
                hash_map[num] = [i + 1]
        for num in numbers:
            aim = target - num
            if aim in hash_map:
                ans = [hash_map[num][0]]
                for index in hash_map[aim]:
                    if index != ans[0]:
                        ans.append(index)
                        break
                return ans

    # 由于是非降list且需要返回具体index，所以双指针比hash快
    @timing
    def twoSum2(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            nl, nr = numbers[l], numbers[r]
            ns = nl + nr
            if ns < target:
                while l < r and numbers[l] == nl:
                    l += 1
            elif ns > target:
                while l < r and numbers[r] == nr:
                    r -= 1
            else:
                return [l + 1, r + 1]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    numbers = [2, 7, 11, 15]
                    target = 9
                case 2:
                    # sample 2
                    numbers = [0, 0, 3, 4]
                    target = 0
                case 3:
                    # sample 3
                    numbers = [-1, 0]
                    target = -1
                case _:
                    break
            print(f"ans = {solution.twoSum(numbers,target)}")
            print(f"ans = {solution.twoSum2(numbers,target)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
