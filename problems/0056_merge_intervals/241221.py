from typing import List


class Solution:
    # 输入不是按照start顺序排列的
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        if n <= 1:
            return intervals
        intervals.sort(key=lambda x: (x[0], -x[1]))
        ans = [intervals[0]]
        for i in range(1, n):
            temp_group = len(ans) - 1
            temp_start, temp_end = ans[temp_group]
            start, end = intervals[i]
            if temp_start == start:
                continue
            if temp_end >= start:
                ans[temp_group][1] = max(temp_end, end)
            else:
                ans.append(intervals[i])
        return ans
