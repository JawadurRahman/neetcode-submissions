class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        infinite = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(i, j, dist):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or grid[i][j] < dist:
                return

            if grid[i][j] > dist:
                grid[i][j] = dist

            dfs(i + 1, j, dist + 1)
            dfs(i - 1, j, dist + 1)
            dfs(i, j + 1, dist + 1)
            dfs(i, j - 1, dist + 1)

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    dfs(i, j, 0)

