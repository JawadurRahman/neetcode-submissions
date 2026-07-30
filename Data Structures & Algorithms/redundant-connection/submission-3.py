class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        hmap = defaultdict(set)
        for a,b in edges:
            hmap[a].add(b)
            hmap[b].add(a)
        
        def dfs(node, parent):
            if node in visited: return False

            visited.add(node)
            for child in hmap[node]:
                if child == parent: continue
                if not dfs(child, node): return False
            return True
                

        while edges:
            visited = set()
            n1, n2 = edges.pop()
            hmap[n1].remove(n2)
            hmap[n2].remove(n1)
            node = n1 if len(hmap[n1]) >= len(hmap[n2]) else n2
            if dfs(node, None) and len(visited) == n:
                return [n1, n2]
            hmap[n1].add(n2)
            hmap[n2].add(n1)
        return []