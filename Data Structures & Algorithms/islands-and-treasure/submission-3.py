class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        infinite = 2147483647
        ROWS = len(grid)
        COLS = len(grid[0])

        gates_location_arr = []
        def bfs():
            nonlocal gates_location_arr
            dq = deque(gates_location_arr)

            while dq:
                row, col, dist = dq.popleft()
                if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] < dist:
                    continue

                if grid[row][col] > dist: grid[row][col] = dist    
                dq.append((row + 1, col, dist + 1))
                dq.append((row - 1, col, dist + 1))
                dq.append((row, col + 1, dist + 1))
                dq.append((row, col - 1, dist + 1))

        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 0:
                    gates_location_arr.append((i, j, 0))
        bfs()
