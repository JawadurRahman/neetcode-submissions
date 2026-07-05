# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0
        def ftn(node: TreeNode, count):
            nonlocal ans
            if node.val >= count: ans += 1
            count = max(count, node.val)
            if node.left: ftn(node.left, count)
            if node.right: ftn(node.right, count)
        ftn(root, -math.inf)
        return ans
