"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited = {} 
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        n = Node(node.val)
        self.visited[node] = n
        for neigh in node.neighbors:
            if neigh in self.visited:
                n.neighbors.append(self.visited[neigh])
            else:
                n.neighbors.append(self.cloneGraph(neigh))
        return n