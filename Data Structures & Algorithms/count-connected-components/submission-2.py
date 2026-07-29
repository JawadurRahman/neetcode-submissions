class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()

        def dfs(i):
            if i in visited: return
            visited.add(i)
            for j in adjList[i]:
                if j not in visited:
                    dfs(j)

        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
            if len(visited) == n: break
        return count
        