from typing import List


class Solution:
    # 由于是非降list且需要返回具体index，所以双指针比hash快
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l, r = 0, n - 1
        while l < r:
            nl, nr = numbers[l], numbers[r]
            ns = nl + nr
            if ns < target:
                while l < r and numbers[l] == nl:
                    l += 1
            elif ns > target:
                while l < r and numbers[r] == nr:
                    r -= 1
            else:
                return [l + 1, r + 1]
