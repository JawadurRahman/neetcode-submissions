class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacificSet = set()
        atlanticSet = set()
        ROWS = len(heights)
        COLS = len(heights[0])
        dq = deque([])

        for i in range(COLS):
            dq.append((0, i))
            pacificSet.add((0, i))
        for i in range(ROWS):
            dq.append((i, 0))
            pacificSet.add((i, 0))
        while dq:
            i,j = dq.popleft()
            for di, dj in [(i + 1, j), (i - 1, j),(i, j + 1),(i, j - 1)]:
                if 0 <= di < ROWS and 0 <= dj < COLS and (di, dj) not in pacificSet \
                    and heights[di][dj] >= heights[i][j]:
                    pacificSet.add((di, dj))
                    dq.append((di, dj))

        for i in range(COLS):
            dq.append((ROWS - 1, i))
            atlanticSet.add((ROWS - 1, i))
        for i in range(ROWS):
            dq.append((i, COLS - 1))
            atlanticSet.add((i, COLS - 1))
        while dq:
            i,j = dq.popleft()
            for di, dj in [(i + 1, j), (i - 1, j),(i, j + 1),(i, j - 1)]:
                if 0 <= di < ROWS and 0 <= dj < COLS and (di, dj) not in atlanticSet \
                    and heights[di][dj] >= heights[i][j]:
                    atlanticSet.add((di, dj))
                    dq.append((di, dj))

        ans = []
        for i,j in atlanticSet.intersection(pacificSet):
            ans.append([i,j])

        return ans
