from typing import List


class Solution:
    # 复制另一个数组的空间复杂度比较高
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        live_neighbour = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i > 0:  # 注意不是1
                    live_neighbour[i][j] += board[i - 1][j]
                    if j > 0:  # 注意不是1
                        live_neighbour[i][j] += board[i - 1][j - 1]

                    if j < m - 1:
                        live_neighbour[i][j] += board[i - 1][j + 1]
                if i < n - 1:
                    live_neighbour[i][j] += board[i + 1][j]
                    if j > 0:  # 注意不是1
                        live_neighbour[i][j] += board[i + 1][j - 1]
                    if j < m - 1:
                        live_neighbour[i][j] += board[i + 1][j + 1]
                if j > 0:  # 注意不是1
                    live_neighbour[i][j] += board[i][j - 1]
                if j < m - 1:
                    live_neighbour[i][j] += board[i][j + 1]
        for i in range(n):
            for j in range(m):
                if board[i][j] == 1 and (
                    live_neighbour[i][j] < 2 or live_neighbour[i][j] > 3
                ):
                    board[i][j] = 0
                if board[i][j] == 0 and live_neighbour[i][j] == 3:
                    board[i][j] = 1
