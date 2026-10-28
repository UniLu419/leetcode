from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
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
