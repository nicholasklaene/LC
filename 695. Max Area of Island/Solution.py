"""
DFS
Time: O(MxN)
Space: O(MxN)
"""

from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        answer = 0
        visited = [[False for j in range(n)] for i in range(m)]

        def inBounds(row, col):
            return row < m and row >= 0 and col < n and col >= 0

        def dfs(row, col):
            if not inBounds(row, col) or visited[row][col] or grid[row][col] == 0:
                return 0
            visited[row][col] = True
            return 1 + (
                dfs(row + 1, col)
                + dfs(row - 1, col)
                + dfs(row, col + 1)
                + dfs(row, col - 1)
            )

        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col] == 1:
                    size = dfs(row, col)
                    answer = max(answer, size)

        return answer
