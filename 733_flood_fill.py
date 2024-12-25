from typing import List
from timing_dec import timing


class Solution:
    @timing
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, color: int
    ) -> List[List[int]]:
        pre_color = image[sr][sc]
        if color == pre_color:
            return image
        n, m = len(image), len(image[0])
        image[sr][sc] = color
        queue = [[sr, sc]]
        while queue:
            current = queue.pop(0)
            x, y = current[0], current[1]
            # top
            if x - 1 >= 0 and image[x - 1][y] == pre_color:
                image[x - 1][y] = color
                queue.append([x - 1, y])
            # bottom
            if x + 1 < n and image[x + 1][y] == pre_color:
                image[x + 1][y] = color
                queue.append([x + 1, y])
            # left
            if y - 1 >= 0 and image[x][y - 1] == pre_color:
                image[x][y - 1] = color
                queue.append([x, y - 1])
            # right
            if y + 1 < m and image[x][y + 1] == pre_color:
                image[x][y + 1] = color
                queue.append([x, y + 1])
        return image


def main():
    # Your main code goes here
    solution = Solution()
    while True:
        try:
            index = int(input("index: "))
            match index:
                case 1:
                    # sample 1
                    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
                    sr = 1
                    sc = 1
                    color = 2
                case 2:
                    # sample 2
                    image = [[0, 0, 0], [0, 0, 0]]
                    sr = 0
                    sc = 0
                    color = 0
                case _:
                    break
            print(f"ans = {solution.floodFill(image,sr,sc,color)}")
        except Exception as e:
            print(f"Error: {e}")
            break


if __name__ == "__main__":
    main()
