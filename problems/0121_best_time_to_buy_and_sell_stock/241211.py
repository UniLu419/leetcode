from copy import copy
from typing import List


class Solution:
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
        max_profit = 0
        for i in range(days):
            profit = max[i] - min[i]
            if profit > max_profit:
                max_profit = profit
        return max_profit
