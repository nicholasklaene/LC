"""
DFS: destroy islands connected to the border,
then explore all remaining islands

Time: O(MxN)
Space: O(MxN)
"""

from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = [[False for j in range(n)] for i in range(m)]

        def inBounds(row: int, col: int) -> bool:
            return row < m and row >= 0 and col < n and col >= 0

        def dfs(row: int, col: int, destroy: bool) -> None:
            if not inBounds(row, col) or visited[row][col] or grid[row][col] == 1:
                return
            visited[row][col] = True
            if destroy:
                grid[row][col] = 1
            dfs(row + 1, col, destroy)
            dfs(row - 1, col, destroy)
            dfs(row, col + 1, destroy)
            dfs(row, col - 1, destroy)

        def destroyBorderIslands():
            for col in range(n):
                dfs(0, col, destroy=True)
                dfs(m - 1, col, destroy=True)
            for row in range(m):
                dfs(row, 0, destroy=True)
                dfs(row, n - 1, destroy=True)

        destroyBorderIslands()

        answer = 0
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 and not visited[row][col]:
                    dfs(row, col, destroy=False)
                    answer += 1

        return answer
