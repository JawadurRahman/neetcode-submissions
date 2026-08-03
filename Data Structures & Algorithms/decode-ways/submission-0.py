class Solution:
    def numDecodings(self, s: str) -> int:
        hmap = {str(i) for i in range(1,27)}
        ans = 0
        cache = defaultdict(int)

        def dfs(index):
            if index in cache: return cache[index]
            if index >= len(s): return 1
            l1 = s[index]
            l2 = None
            if index < len(s) - 1: l2 = s[index] + s[index + 1]
            if l1 in hmap: cache[index] += dfs(index + 1)
            if l2 in hmap: cache[index] += dfs(index + 2)
            return cache[index]

        return dfs(0)