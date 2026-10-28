from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        n = len(intervals)
        if n == 0:
            return [newInterval]
        ans: List[List[int]] = []
        # 记录start是否插入
        found = False
        for i, interval in enumerate(intervals):
            # 左边不重合区间插入
            if interval[1] < newInterval[0]:
                ans.append(interval)
                continue
            # 找到start落在哪个区间里
            if not found:
                # 如果不重合 直接插入
                if newInterval[1] < interval[0]:
                    ans.append(newInterval)
                    ans.append(interval)  # 不要忘记处理当前interval
                else:  # 如果重合 合并后插入
                    ans.append(
                        [
                            min(interval[0], newInterval[0]),
                            max(interval[1], newInterval[1]),
                        ]
                    )
                found = True  # 注意更新条件
            # 已经插入了，end可能会影响后续区间
            else:
                # 如果和最后一个插入区间重合
                if interval[0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], interval[1])
                else:
                    ans.append(interval)
        # start不落在任何区间里
        if not found:
            ans.append(newInterval)
        return ans
