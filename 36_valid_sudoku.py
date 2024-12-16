from typing import List
from timing_dec import timing
from math import ceil


class Solution:
    @timing
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        hash_row, hash_col, hash_sqr = [], [], []
        # 对数组的行列方块建哈希表
        for i in range(9):
            hash_row.append({})
            hash_col.append({})
            hash_sqr.append({})

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num == ".":
                    continue
                row = ceil((i + 1) / 3)
                col = ceil((j + 1) / 3)
                sqr_num = (row - 1) * 3 + col - 1
                if num in hash_row[i] or num in hash_col[j] or num in hash_sqr[sqr_num]:
                    return False
                hash_row[i][num] = True
                hash_col[j][num] = True
                hash_sqr[sqr_num][num] = True
        return True


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    board = [
                        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                    ]
                case 2:
                    # sample 2
                    board = [
                        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
                        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                        [".", "9", "8", ".", ".", ".", ".", "6", "."],
                        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                        [".", "6", ".", ".", ".", ".", "2", "8", "."],
                        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
                    ]
                case _:
                    break
            print(f"ans = {solution.isValidSudoku(board)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()

# [{}] * 9 这种写法会导致所有的{}指向同一个地址
# [{} for i in range(9)] 这种写法的话{}指向的地址是不同的
# for i in range(9):
#   hash_row.append({}) 这种写法的话{}指向的地址是不同的
