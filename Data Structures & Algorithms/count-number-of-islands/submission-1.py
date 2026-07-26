class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        ROWS = len(grid)
        COLS = len(grid[0])
            
        for y, row in enumerate(grid):
            for x, digit in enumerate(row):
                if digit == "1":
                    dq = [(y, x)]
                    while dq:
                        i, j = dq.pop()
                        grid[i][j] = "0"
                        for i2,j2 in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                            if 0 <= i2 < ROWS and 0 <= j2 < COLS and grid[i2][j2] == "1":
                                dq.append((i2, j2))
                    count += 1
        return count
