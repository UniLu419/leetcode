from typing import List
from math import floor


class Solution:
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
