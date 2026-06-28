"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldToCopy = {None: None}
        node = head
        while node:
            oldToCopy[node] = Node(node.val)
            node = node.next

        node = head
        while node:
            oldToCopy[node].random = oldToCopy[node.random]
            oldToCopy[node].next = oldToCopy[node.next]
            node = node.next
            
        return oldToCopy[head]
