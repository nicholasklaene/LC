"""
DFS Solution
Time: O(MxN)
Space: O(MxN) - recursion takes extra memory
"""

from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        m, n = len(image), len(image[0])

        def inBounds(row, col):
            return row < m and row >= 0 and col < n and col >= 0

        colorToChange = image[sr][sc]

        def dfs(row, col):
            if not inBounds(row, col) or image[row][col] != colorToChange:
                return

            image[row][col] = newColor

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        if colorToChange != newColor:
            dfs(sr, sc)

        return image
