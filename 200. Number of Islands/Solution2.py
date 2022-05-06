"""
DFS with visited
Time: O(MxN)
Space: O(MxN)
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])

        def inBounds(row, col):
            return row < m and row >= 0 and col < n and col >= 0

        visited = [[False for j in range(n)] for i in range(m)]

        def dfs(row, col):
            if not inBounds(row, col) or visited[row][col] or grid[row][col] == "0":
                return

            visited[row][col] = True

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        answer = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == "1" and not visited[row][col]:
                    dfs(row, col)
                    answer += 1

        return answer
