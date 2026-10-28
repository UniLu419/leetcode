from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                max += profit
        return max
