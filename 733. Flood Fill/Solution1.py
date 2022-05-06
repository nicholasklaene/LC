"""
BFS Solution
Time: O(MxN)
Space: O(MxN)
"""

from typing import List
from collections import deque


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        def inBounds(row, col):
            return row < len(image) and row >= 0 and col < len(image[0]) and col >= 0

        q = deque()
        q.append((sr, sc))
        colorToChange = image[sr][sc]

        if colorToChange == newColor:
            return image

        while len(q) > 0:
            row, col = q.popleft()
            if inBounds(row, col) and image[row][col] == colorToChange:
                image[row][col] = newColor
                q.extend(
                    [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
                )

        return image
