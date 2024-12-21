from typing import List
from timing_dec import timing


class Solution:
    @timing
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        if n < 1:  # 注意空输入
            return []
        ans = [[nums[0]]]
        for i in range(1, n):
            # 拿出ans最后一组看，如果nums[i]和最后一个相邻，就append到最后，否则append一个list到ans里，第一位是nums[i]
            temp_group = len(ans) - 1
            temp_len = len(ans[temp_group])
            temp = ans[temp_group][temp_len - 1]
            if temp + 1 == nums[i]:
                ans[temp_group].append(nums[i])
            else:
                ans.append([nums[i]])
        return [
            f"{group[0]}" if len(group) == 1 else f"{group[0]}->{group[len(group)-1]}"
            for group in ans
        ]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    nums = [0, 1, 2, 4, 5, 7]
                case 2:
                    # sample 2
                    nums = [0, 2, 3, 4, 6, 8, 9]
                case _:
                    break
            print(f"ans = {solution.summaryRanges(nums)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
