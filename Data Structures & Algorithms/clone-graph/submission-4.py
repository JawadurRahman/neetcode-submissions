"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        visited = {}
        n = Node(node.val)
        dq = deque([node])
        visited[node] = n

        while dq:
            node = dq.popleft()
            
            for neigh in node.neighbors:
                if neigh not in visited:
                    clone_neigh = Node(neigh.val)
                    visited[neigh] = clone_neigh
                    dq.append(neigh)
                visited[node].neighbors.append(visited[neigh])
                    
        return n