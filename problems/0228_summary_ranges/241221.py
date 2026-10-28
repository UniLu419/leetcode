from typing import List


class Solution:
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
