# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        dq = deque([root])
        while dq:
            for i in range(len(dq)):
                node = dq.popleft()
                arr.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
        
        arr.sort()
        return arr[k-1]