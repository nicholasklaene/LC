"""
DFS: solve number of islands but keep
a bool value indicating whether the island
is still a valid subisland. In this case, since
the matrix is binary, I used boolean & instead of logical
and, but the result would be the same.

Time: O(MxN)
Space: O(MxN) - recursion + visited
"""

from typing import List


class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])

        def inBounds(row: int, col: int) -> bool:
            return row < m and row >= 0 and col < n and col >= 0

        visited = [[False for j in range(n)] for i in range(m)]

        def isSubIsland(row: int, col: int) -> int:
            if not inBounds(row, col) or visited[row][col] or grid2[row][col] == 0:
                return 1
            visited[row][col] = True
            return (
                grid1[row][col]
                & isSubIsland(row + 1, col)
                & isSubIsland(row - 1, col)
                & isSubIsland(row, col + 1)
                & isSubIsland(row, col - 1)
            )

        answer = 0
        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid2[row][col] == 1:
                    answer += isSubIsland(row, col)

        return answer
