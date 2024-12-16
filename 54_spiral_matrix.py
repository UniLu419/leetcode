from typing import List
from timing_dec import timing


class Solution:
    @timing
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i, j, count, total = 0, 0, 0, 0
        row_length = len(matrix)
        col_length = len(matrix[0])
        total = row_length * col_length
        status = [[True for _ in range(col_length)] for _ in range(row_length)]
        ans = []
        while count < total:
            while j < col_length and status[i][j]:
                print(f"status[{i}][{j}]: {status[i][j]}")
                ans.append(matrix[i][j])
                status[i][j] = False
                count += 1
                j += 1
            j -= 1  # 将出界的坐标回调
            i += 1  # 跳过已处理过的坐标
            while i < row_length and status[i][j]:
                print(f"status[{i}][{j}]: {status[i][j]}")
                ans.append(matrix[i][j])
                status[i][j] = False
                count += 1
                i += 1
            i -= 1
            j -= 1
            while j >= 0 and status[i][j]:  # 注意边界条件有等号
                print(f"status[{i}][{j}]: {status[i][j]}")
                ans.append(matrix[i][j])
                status[i][j] = False
                count += 1
                j -= 1
            j += 1
            i -= 1
            while i >= 0 and status[i][j]:
                print(f"status[{i}][{j}]: {status[i][j]}")
                ans.append(matrix[i][j])
                status[i][j] = False
                count += 1
                i -= 1
            i += 1
            j += 1  # 注意不要漏掉和下一个循环里的第一个while的衔接
        return ans


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
                    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
                case _:
                    break
            print(f"ans = {solution.spiralOrder(matrix)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
