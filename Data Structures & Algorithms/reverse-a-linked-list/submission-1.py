# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [None]
        while head:
            nxt = head.next
            head.next = None
            arr.append(head)
            arr[-1].next = arr[-2]
            head = nxt

        return arr[-1]