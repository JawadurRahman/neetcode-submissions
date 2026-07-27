class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] == 0:
                return 0

            grid[i][j] = 0
            return 1 + dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            
        for i, row in enumerate(grid):
            for j, num in enumerate(row):
                if num == 1:
                    ans = max(ans, dfs(i, j))

        return ans