from re import L
from typing import Counter, List
from timing_dec import timing


class Solution:
    @timing
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        hash_map = {}
        calculated = [False for _ in nums]
        for i, num in enumerate(nums):
            hash_map[num] = i

        for i, num in enumerate(nums):
            if calculated[i]:
                continue
            target = num + 1
            temp = 1
            while target in hash_map:
                calculated[hash_map[target]] = True
                temp += 1
                target += 1
            target = num - 1
            while target in hash_map:
                calculated[hash_map[target]] = True
                temp += 1
                target -= 1
            if temp > longest:
                longest = temp
        return longest

    @timing
    def longestConsecutive2(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        nums = sorted(nums)
        cur_max, ans_max = 1, 0
        for i in range(1, n):
            pre = nums[i - 1]
            if pre == nums[i]:
                continue
            elif pre + 1 == nums[i]:
                cur_max += 1
            else:
                if cur_max > ans_max:
                    ans_max = cur_max
                cur_max = 1
        if cur_max > ans_max:  # 不要忘记最后一个
            ans_max = cur_max
        return ans_max


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [100, 4, 200, 1, 3, 2]
                case 2:
                    # sample 2
                    nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
                case _:
                    break
            print(f"ans = {solution.longestConsecutive(nums)}")
            print(f"ans = {solution.longestConsecutive2(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
