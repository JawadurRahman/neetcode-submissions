# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        total = 0
        tens = 1
        while l1 and l2:
            s = l1.val + l2.val
            total += s * tens
            tens *= 10
            l1 = l1.next
            l2 = l2.next
        
        while l1:
            total += l1.val * tens
            tens *= 10
            l1 = l1.next

        while l2:
            total += l2.val * tens
            tens *= 10
            l2 = l2.next

        dummy = ListNode(0)
        ans = dummy
        if total == 0: return dummy
        while total != 0:
            md = total % 10
            total //= 10
            digit = ListNode(md)
            dummy.next = digit
            dummy = dummy.next
        
        return ans.next

        