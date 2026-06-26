# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        start = head
        dq = deque([])
        while start:
            temp = start
            start = start.next
            temp.next = None
            dq.append(temp)
        
        dummy = ListNode()
        while dq:
            left = dq.popleft()
            dummy.next = left
            right = None
            if dq: 
                right = dq.pop()
            left.next = right
            dummy = right
