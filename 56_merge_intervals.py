from typing import List
from timing_dec import timing


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
                case 2:
                    # sample 2
                    intervals = [[1, 4], [4, 5]]
                case _:
                    break
            print(f"ans = {solution.merge(intervals)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
