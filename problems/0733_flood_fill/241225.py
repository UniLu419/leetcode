from typing import List


class Solution:
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
