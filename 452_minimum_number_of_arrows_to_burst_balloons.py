from typing import List
from timing_dec import timing


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    points = [[10, 16], [2, 8], [1, 6], [7, 12]]
                case 2:
                    # sample 2
                    points = [[1, 2], [3, 4], [5, 6], [7, 8]]
                case 3:
                    # sample 3
                    points = [[1, 2], [2, 3], [3, 4], [4, 5]]
                case _:
                    break
            print(f"ans = {solution.findMinArrowShots(points)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
