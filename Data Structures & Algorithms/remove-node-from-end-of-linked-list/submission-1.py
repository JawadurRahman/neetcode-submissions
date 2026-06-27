# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        dummy = head
        while dummy:
            dummy = dummy.next
            count += 1
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        i = 0
        while curr:
            if i == count - n:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr = curr.next
            i += 1
        return dummy.next
            