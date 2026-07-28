class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dq = deque([])
        good_bananas = 0
        
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == 2:
                    dq.append((i, j))
                if cell == 1: good_bananas += 1
        if good_bananas == 0: return 0
        
        time = -1
        while dq:
            for _ in range(len(dq)):
                i, j = dq.popleft()

                for di, dj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0 <= di < ROWS and 0 <= dj < COLS and grid[di][dj] == 1:
                        grid[di][dj] = 2
                        good_bananas -= 1
                        dq.append((di, dj))
                
            time += 1
        
        return time if good_bananas == 0 else -1



                    