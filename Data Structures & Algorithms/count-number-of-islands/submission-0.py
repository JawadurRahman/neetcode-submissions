class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        def dfs(x, y):
            if y >= ROWS or x >= COLS or x < 0 or y < 0 \
            or grid[y][x] == "0":
                return

            grid[y][x] = "0"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
            
        for y, row in enumerate(grid):
            for x, digit in enumerate(row):
                if digit == "1":
                    dfs(x, y)
                    count += 1
        return count
