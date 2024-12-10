from copy import copy
from typing import List
from timing_dec import timing


class Solution:
    @timing
    def maxProfit(self, prices: List[int]) -> int:
        days = len(prices)
        max = copy(prices)
        min = copy(prices)
        for i in range(1, days):
            if prices[days - 1 - i] < max[days - i]:
                max[days - 1 - i] = max[days - i]
            else:
                max[days - 1 - i] = prices[days - 1 - i]
            if prices[i] < min[i - 1]:
                min[i] = prices[i]
            else:
                min[i] = min[i - 1]
            print(f"max: {max}")
            print(f"min: {min}")
        max_profit = 0
        for i in range(days):
            profit = max[i] - min[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit

    @timing
    def maxProfit2(self, prices: List[int]) -> int:
        max = 0
        min = prices[0]
        for price in prices:
            if price < min:
                min = price
            if price - min > max:
                max = price - min
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
                    prices = [7, 1, 5, 3, 6, 4]
                case 2:
                    # sample 2
                    prices = [7, 6, 4, 3, 1]
                case _:
                    break
            print(f"ans = {solution.maxProfit(prices)}")
            print(f"ans = {solution.maxProfit2(prices)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
