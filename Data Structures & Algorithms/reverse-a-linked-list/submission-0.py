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
            head = nxt

        for i in range(len(arr) - 1, 0, -1):
            arr[i].next = arr[i - 1]

        return arr[-1]