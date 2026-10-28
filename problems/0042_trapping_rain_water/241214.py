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
        highest = [min(l, r) - h for l, r, h in zip(left, right, height)]
        return sum(highest)
