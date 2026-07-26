class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        used = set()
        def dfs(y, x, index):
            if index == len(word) - 1:
                return True
            found = False
            for yp, xp in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                if 0 <= y + yp < len(board) and 0 <= x + xp < len(board[0]):
                    if (y + yp, x + xp) not in used and board[y + yp][x + xp] == word[index + 1]:
                        used.add((y + yp, x + xp))
                        found = found or dfs(y + yp, x + xp, index + 1)
                        used.remove((y + yp, x + xp))
            return found

        ans = False
        for y, row in enumerate(board):
            for x, letter in enumerate(row):
                if letter == word[0]:
                    used.add((y, x))
                    ans = ans or dfs(y, x, 0)
                    used.remove((y, x))
                    if ans == True:
                        return True

        return ans