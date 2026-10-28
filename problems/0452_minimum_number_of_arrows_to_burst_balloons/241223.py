from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        ans = []
        n = len(points)
        if n <= 1:
            return n
        i = 0
        while i < n:
            # compare with the previous union.
            # if no overlapping, calculate the next overlap union,if no overlap and the next array
            # else manage the last overlap union
            if not ans or ans[-1][1] < points[i][0]:
                if i + 1 < n and points[i][1] >= points[i + 1][0]:  # 注意大小于
                    ans.append([points[i + 1][0], min(points[i][1], points[i + 1][1])])
                    i += 2
                else:
                    ans.append(points[i])
                    i += 1
            else:
                ans[-1][0] = max(ans[-1][0], points[i][0])
                ans[-1][1] = min(ans[-1][1], points[i][1])
                i += 1
        return len(ans)
