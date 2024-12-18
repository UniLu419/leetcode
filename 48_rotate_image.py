from typing import List
from timing_dec import timing
from math import floor


class Solution:
    @timing
    def rotate(self, matrix: List[List[int]]) -> None:
        # 对于一个边长为n的矩阵，它需要旋转的层数为floor((n-1)//2)
        n = len(matrix[0])
        # range(rotate_layers)不包含 rotate_layers所以取 1-index 个数
        rotate_layers = floor(n / 2)
        # 对于第i层，边长为n-2i，起始点为（i，i），终点为（n - i，n - i），也是因为这个原因，单个数换比整行换更好写
        for i in range(rotate_layers):
            # 由于第一行的最后一个数是右列第一个数，不用再换，不要忘记-1
            for y in range(i, n - i - 1):
                current = matrix[i][y]
                # 上行换至右列， 从上向下换，正序y
                matrix[y][n - i - 1], current = current, matrix[y][n - i - 1]
                # 右列换至下行，从右向左换，倒序y
                matrix[n - i - 1][n - 1 - y], current = (
                    current,
                    matrix[n - i - 1][n - 1 - y],
                )
                # 下行换至左列，从下向上换，倒序y
                matrix[n - 1 - y][i], current = current, matrix[n - 1 - y][i]
                # 左列换至上行，从左向右换，正序y
                matrix[i][y], current = current, matrix[i][y]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                case 2:
                    # sample 2
                    matrix = [
                        [5, 1, 9, 11],
                        [2, 4, 8, 10],
                        [13, 3, 6, 7],
                        [15, 14, 12, 16],
                    ]
                case _:
                    break
            print(f"ans = {solution.rotate(matrix)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
