# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = k
        ans = -1
        def inorder(node):
            nonlocal ans
            nonlocal count
            if node.left: inorder(node.left)
            count -= 1
            if count == 0:
                ans = node.val
                return
            if node.right: inorder(node.right)

        inorder(root)
        return ans

            

                