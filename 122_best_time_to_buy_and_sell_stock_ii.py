from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        for i in range(len(prices) - 1):
            profit = prices[i + 1] - prices[i]
            if profit > 0:
                max += profit
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
                    prices = [1, 2, 3, 4, 5]
                case 3:
                    # sample 3
                    prices = [7, 6, 4, 3, 1]
                case _:
                    break
            print(f"ans = {solution.maxProfit(prices)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
