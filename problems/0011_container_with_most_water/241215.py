from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l, r = 0, n - 1
        max = 0
        while l < r:
            hl, hr = height[l], height[r]
            vol = min(hl, hr) * (r - l)
            if vol > max:
                max = vol
            # 越往中间x边越短，所以只有更高才有可能更新最大值
            if hl < hr:
                while l < r and height[l] <= hl:
                    l += 1
            else:
                while l < r and height[r] <= hr:
                    r -= 1
        return max
