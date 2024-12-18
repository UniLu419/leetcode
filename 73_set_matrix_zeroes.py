from typing import List
from timing_dec import timing


class Solution:
    @timing
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        row, col = {}, {}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row[i] = True
                    col[j] = True
        for key in row.keys():
            for j in range(m):
                matrix[key][j] = 0
        for key in col.keys():
            for i in range(n):
                matrix[i][key] = 0


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
                case 2:
                    # sample 2
                    matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
                case _:
                    break
            print(f"ans = {solution.setZeroes(matrix)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
