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
        if not head: return None
        start = head
        mp = {None: -1}
        mp2 = {-1: None}
        dummy = Node(start.val)
        mp[start] = 0
        mp2[0] = dummy
        start = start.next
        count = 1
        while start:
            dummy.next = Node(start.val)
            dummy = dummy.next
            mp2[count] = dummy
            mp[start] = count          
            start = start.next
            count += 1

        start = head
        dummy = mp2[0]
        while start:
            dummy.random = mp2[mp[start.random]]
            dummy = dummy.next
            start = start.next


        return mp2[0]
