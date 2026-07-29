class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        visited = set()
        seen = set()

        def dfs(i, last):
            if i in visited: return False
            seen.add(i)
            visited.add(i)
            for j in adjList[i]:
                if j == last: continue
                if not dfs(j, i): return False
            visited.remove(i)
            return True

        if not dfs(0, None):
            return False

        return len(seen) == n
