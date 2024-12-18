from typing import List
from timing_dec import timing


class Solution:
    # 复制另一个数组的空间复杂度比较高
    @timing
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

    # 为了减少空间开销，我们可以令之前为0，之后为1的cell变成2，之前为1之后为0的cell变成-1
    @timing
    def gameOfLife2(self, board: List[List[int]]) -> None:
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


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
                case 2:
                    # sample 2
                    board = [[1, 1], [1, 0]]
                case _:
                    break
            print(f"ans = {solution.gameOfLife(board)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
