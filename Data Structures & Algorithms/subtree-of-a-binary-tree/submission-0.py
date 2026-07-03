# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        same = False
        if root.val == subRoot.val:
            same = self.isSameTree(root, subRoot)
        
        ls, rs = False, False
        if root.left:
            ls = self.isSubtree(root.left, subRoot)
        if root.right:
            rs = self.isSubtree(root.right, subRoot)

        return same or ls or rs

        
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # if not p and not q: return True
        if p and not q: return False
        if q and not p: return False
        if not p and not q: return True
        lt = self.isSameTree(p.left, q.left)
        rt = self.isSameTree(p.right, q.right)
        return p.val == q.val and lt and rt
