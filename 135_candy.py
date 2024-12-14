from typing import List
from timing_dec import timing


class Solution:
    @timing
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        for i in range(1, n):
            if (
                ratings[n - 1 - i] > ratings[n - i]
                and candies[n - 1 - i] <= candies[n - i]  # 不要忘记等于！
            ):
                candies[n - 1 - i] = candies[n - i] + 1
        return sum(candies)


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    ratings = [1, 0, 2]
                case 2:
                    # sample 2
                    ratings = [1, 2, 2]
                case _:
                    break
            print(f"ans = {solution.candy(ratings)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()


# 这道题要求给站成一排的孩子们分配糖果，要满足两个条件：一是每个孩子至少有一颗糖果；二是评分更高的孩子比其相邻的孩子得到更多的糖果。我们可以采用两次遍历的方法来解决这个问题：
# 从左到右遍历：
# 初始化一个长度和 ratings 数组相同的列表 candies，元素初始值都设为 1，表示每个孩子最开始至少有 1 颗糖果。
# 从左到右遍历 ratings 数组，如果当前孩子的评分大于前一个孩子的评分（ratings[i] > ratings[i - 1]），那么就给当前孩子分配比前一个孩子多 1 颗的糖果（candies[i] = candies[i - 1] + 1）。这样就初步保证了左边评分高的孩子糖果比左边相邻孩子多。
# 从右到左遍历：
# 再次遍历 ratings 数组，这次从右到左。如果当前孩子的评分大于后一个孩子的评分（ratings[i] > ratings[i + 1]），并且当前孩子的糖果数小于等于后一个孩子的糖果数（candies[i] <= candies[i + 1]），那就更新当前孩子的糖果数，使其比后一个孩子多 1 颗（candies[i] = candies[i + 1] + 1）。这样就保证了右边评分高的孩子糖果比右边相邻孩子多，并且在两次遍历后，综合考虑了两边相邻的情况，使得每个孩子的糖果分配满足题目要求。
# 计算糖果总数：
# 最后遍历 candies 列表，将所有元素相加，得到分配糖果的最少总数并返回。
