from calendar import c
import json
from typing import List


class Solution:
    def highestRankedKItems(
        self, grid: List[List[int]], pricing: List[int], start: List[int], k: int
    ) -> List[List[int]]:
        row_length = len(grid)
        col_length = len(grid[0])
        distance: List[List[int]] = [
            [-1 for _ in range(col_length)] for _ in range(row_length)
        ]
        distance[start[0]][start[1]] = 0
        queue: List[List[int]] = [start]
        cells: List[List[int]] = []
        current_distance = 0
        if (
            grid[start[0]][start[1]] >= pricing[0]
            and grid[start[0]][start[1]] <= pricing[1]
        ):
            cells.append(start)
            print(f"cells appended: {start}")
        while len(queue) > 0:
            current = queue.pop(0)
            row = current[0]
            col = current[1]
            print(f"previous distance: {current_distance}")
            print(f"current row: {row}")
            print(f"current col: {col}")
            if current_distance < distance[row][col] and len(cells) >= k:
                print(f"TopK found: {cells}")
                break
            current_distance = distance[row][col]
            print(f"current distance: {current_distance}")
            if row - 1 >= 0:
                if grid[row - 1][col] != 0 and distance[row - 1][col] == -1:
                    distance[row - 1][col] = current_distance + 1
                    queue.append([row - 1, col])
                    print(f"top cell distance: {distance[row - 1][col]}")
                    print(f"top cell price: {grid[row - 1][col]}")
                    if (
                        grid[row - 1][col] >= pricing[0]
                        and grid[row - 1][col] <= pricing[1]
                    ):
                        cells.append([row - 1, col])
                        print(f"cells appended: {[row - 1, col]}")
            if col - 1 >= 0:
                if grid[row][col - 1] != 0 and distance[row][col - 1] == -1:
                    distance[row][col - 1] = current_distance + 1
                    queue.append([row, col - 1])
                    print(f"left cell distance: {distance[row][col - 1]}")
                    print(f"left cell price: {grid[row][col - 1]}")
                    if (
                        grid[row][col - 1] >= pricing[0]
                        and grid[row][col - 1] <= pricing[1]
                    ):
                        cells.append([row, col - 1])
                        print(f"cells appended: {[row, col - 1]}")
            if row + 1 < row_length:
                if grid[row + 1][col] != 0 and distance[row + 1][col] == -1:
                    distance[row + 1][col] = current_distance + 1
                    queue.append([row + 1, col])
                    print(f"below cell distance: {distance[row + 1][col]}")
                    print(f"below cell price: {grid[row + 1][col]}")
                    if (
                        grid[row + 1][col] >= pricing[0]
                        and grid[row + 1][col] <= pricing[1]
                    ):
                        cells.append([row + 1, col])
                        print(f"cells appended: {[row + 1, col]}")
            if col + 1 < col_length:
                if grid[row][col + 1] != 0 and distance[row][col + 1] == -1:
                    distance[row][col + 1] = current_distance + 1
                    queue.append([row, col + 1])
                    print(f"right cell distance: {distance[row][col + 1]}")
                    print(f"right cell price: {grid[row][col + 1]}")
                    if (
                        grid[row][col + 1] >= pricing[0]
                        and grid[row][col + 1] <= pricing[1]
                    ):
                        cells.append([row, col + 1])
                        print(f"cells appended: {[row, col + 1]}")
        print(f"cells: {cells}")
        cells.sort(key=lambda x: (distance[x[0]][x[1]], grid[x[0]][x[1]], x[0], x[1]))
        print(f"cells_sorted: {cells}")
        return cells if len(cells) <= k else cells[:k]


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    grid = [[1, 2, 0, 1], [1, 3, 0, 1], [0, 2, 5, 1]]
                    pricing = [2, 3]
                    start = [0, 0]
                    k = 3
                case 2:
                    # sample 2
                    grid = [[1, 2, 0, 1], [1, 3, 3, 1], [0, 2, 5, 1]]
                    pricing = [2, 3]
                    start = [2, 3]
                    k = 2
                case 3:
                    # sample 3
                    grid = [[1, 1, 1], [0, 0, 1], [2, 3, 4]]
                    pricing = [2, 3]
                    start = [0, 0]
                    k = 3
                case 4:
                    # sample 4
                    grid = [[0, 2, 0]]
                    pricing = [2, 2]
                    start = [0, 1]
                    k = 1
                case _:
                    break

            print(f"ans = {solution.highestRankedKItems(grid,pricing,start,k)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()


"""
解题思路：
    - 这道题的起始点不是固定[0,0]所以不能直接用传统动规的双重循环写，考虑Dijkstra最短路：
        - 维护一个存储最短距离的矩阵，大小与原矩阵相同，使用-1作为默认值表示无穷大，其中start点的distance矩阵值为0
        - 维护一个已计算distance队列queue，初始值为[start]
        - 对于每一个queue中pop出的点，已有最短路距离，所以可以进一步处理上下左右相邻点：
            - 若该点可达（grid不为0）且未被处理过（distance为-1）则计算最短路并加入queue
    - 最终会得到一个计算完毕的distance矩阵
    - 然而这道题需要根据pricing区间判断该点是否available，所以在以上的Dijkstra中，我们可以增加一个队列cells来维护被选中的点：
        - 在每一个计算距离的地方加入if判断grid值是否在pricing区间内，若满足条件则将当前坐标加入cells（不要忘记初始化distance时的start点）
    - 我们最后要输出的值只需要topK，所以显然这里是可以进行剪枝优化的：
        - 由于第一判断条件为distance，所以我们只需要在每次distance+1的时候去判断当前cells是否满k个需要break
    - 得到的cells是按照distance排序，所以我们需要加上其他判断条件来进一步排序（cells.sort()）
    - 判断是否满k个，不满则全部输出，否则输出前k个
错误点：
    - 读题漏读有不可通过点，用了普通循环没用动规
    - 判断价格的时候漏加上下界值
    - 初始点是否符合价格要求忘记判断
"""
