"""
DFS: destroy islands connected to the border,
then count how many 1 cells are reamining

Time: O(MxN) - visit every single cell 
Space: O(MxN) - recursion
"""

from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def destroyLandConnectedIslands() -> None:
            def inBounds(row: int, col: int) -> bool:
                return row < m and row >= 0 and col < n and col >= 0

            def destroy(row: int, col: int) -> None:
                if not inBounds(row, col) or grid[row][col] == 0:
                    return
                grid[row][col] = 0
                destroy(row + 1, col)
                destroy(row - 1, col)
                destroy(row, col + 1)
                destroy(row, col - 1)

            for col in range(n):
                destroy(0, col)
                destroy(m - 1, col)

            for row in range(m):
                destroy(row, 0)
                destroy(row, n - 1)

        def countRemainingLand() -> int:
            answer = 0
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == 1:
                        answer += 1
            return answer

        destroyLandConnectedIslands()
        return countRemainingLand()
