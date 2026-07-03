# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxCount = 0
        if not root: return 0
        def ftn(node: TreeNode):
            nonlocal maxCount
            left, right = 0, 0
            if node.left: 
                left = 1 + ftn(node.left)
            if node.right:
                right = 1 + ftn(node.right)
            maxCount = max(maxCount, left + right)
            return max(left, right)
        
        ftn(root)
        return maxCount