from typing import List
from timing_dec import timing


class Solution:
    @timing
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
                case 2:
                    # sample 2
                    height = [1, 1]
                case _:
                    break
            print(f"ans = {solution.maxArea(height)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
