from typing import List
from timing_dec import timing


class Solution:
    @timing
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [h for h in height]
        right = [h for h in height]
        for i in range(1, n):
            if left[i] < left[i - 1]:
                left[i] = left[i - 1]
            if right[n - 1 - i] < right[n - i]:
                right[n - 1 - i] = right[n - i]
        highest = [min(l, r) - h for l, r, h in zip(left, right, height)]
        return sum(highest)

    @timing
    def trap2(self, height: List[int]) -> int:
        n = len(height)
        left = [h for h in height]
        right = [h for h in height]
        for i in range(1, n):
            if left[i] < left[i - 1]:
                left[i] = left[i - 1]
            if right[n - 1 - i] < right[n - i]:
                right[n - 1 - i] = right[n - i]
        result = 0
        for i in range(n):
            result += min(left[i], right[i]) - height[i]
        return result

    @timing
    def trap3(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_left, max_right, total = 0, 0, 0
        while left < right:
            if height[left] < height[right]:
                if max_left < height[left]:
                    max_left = height[left]
                else:
                    total += max_left - height[left]
                left += 1
            else:
                if max_right < height[right]:
                    max_right = height[right]
                else:
                    total += max_right - height[right]
                right -= 1
        return total


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
                case 2:
                    # sample 2
                    height = [4, 2, 0, 3, 2, 5]
                case _:
                    break
            print(f"ans = {solution.trap(height)}")
            print(f"ans = {solution.trap2(height)}")
            print(f"ans = {solution.trap3(height)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()


# 这类需要计算左右最大高度的最小值的题，第一反应是从左到右取最大值，再从右到左取最大值，然后比较两者最小值，往往可以简化为维护单方向最大值，根据具体情况判断左右处理顺序
