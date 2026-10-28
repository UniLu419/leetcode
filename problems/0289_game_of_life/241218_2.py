from typing import List


class Solution:
    # 为了减少空间开销，我们可以令之前为0，之后为1的cell变成2，之前为1之后为0的cell变成-1
    def gameOfLife(self, board: List[List[int]]) -> None:
        n = len(board)
        m = len(board[0])
        direction = [
            [-1, -1],
            [-1, 0],
            [-1, 1],
            [0, 1],
            [0, -1],
            [1, -1],
            [1, 0],
            [1, 1],
        ]
        for i in range(n):
            for j in range(m):
                live_cnt = self.get_live_cnt(board, i, j, n, m, direction)
                if board[i][j] == 1 and (live_cnt < 2 or live_cnt > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and live_cnt == 3:
                    board[i][j] = 2
        for i in range(n):
            for j in range(m):
                if board[i][j] == -1:
                    board[i][j] = 0
                if board[i][j] == 2:
                    board[i][j] = 1

    def get_live_cnt(
        self,
        board: List[List[int]],
        x: int,
        y: int,
        n: int,
        m: int,
        direction: List[List[int]],
    ):
        cnt = 0
        for i, j in direction:
            new_x, new_y = x + i, y + j
            if new_x < 0 or new_x >= n or new_y < 0 or new_y >= m:  # 不要漏了上限的等号
                continue
            if board[new_x][new_y] == 1 or board[new_x][new_y] == -1:
                cnt += 1
        return cnt
