from typing import List
from timing_dec import timing


class Solution:
    @timing
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
                print(f"{interval[0]} <= {ans[-1][1]} : {interval[0] <= ans[-1][1]}")
                # 如果和最后一个插入区间重合
                if interval[0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], interval[1])
                else:
                    ans.append(interval)
        # start不落在任何区间里
        if not found:
            ans.append(newInterval)
        return ans

    @timing
    def insert2(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key=lambda x: (x[0]))
        n = len(intervals)
        ans = [intervals[0]]
        for i in range(1, n):
            if intervals[i][0] <= ans[-1][1]:
                ans[-1][1] = max(ans[-1][1], intervals[i][1])
            else:
                ans.append(intervals[i])
        return ans


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    intervals = [[1, 3], [6, 9]]
                    newInterval = [2, 5]
                case 2:
                    # sample 2
                    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
                    newInterval = [4, 8]
                case 3:
                    # sample 3
                    intervals = []
                    newInterval = [5, 7]
                case 4:
                    # sample 4
                    intervals = [[1, 5]]
                    newInterval = [6, 8]
                case 5:
                    # sample 5
                    intervals = [[1, 5]]
                    newInterval = [0, 0]
                case 6:
                    # sample 6
                    intervals = [[3, 5], [12, 15]]
                    newInterval = [6, 6]
                case _:
                    break
            print(f"ans = {solution.insert(intervals,newInterval)}")
            print(f"ans = {solution.insert2(intervals,newInterval)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
