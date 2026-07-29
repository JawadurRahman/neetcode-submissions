class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = defaultdict(set)
        for a,b in edges:
            adjList[a].add(b)
            adjList[b].add(a)
        visited = set()

        def dfs(i, last):
            if i in visited: return False
            visited.add(i)
            for j in adjList[i]:
                if j == last: continue
                if not dfs(j, i): return False
            return True


        return dfs(0, None) and len(visited) == n
