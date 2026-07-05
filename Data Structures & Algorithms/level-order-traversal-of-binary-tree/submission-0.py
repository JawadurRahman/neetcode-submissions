# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        dq = deque([root])
        ans = []
        while dq:
            temp = []
            for i in range(len(dq)):
                node = dq.popleft()
                temp.append(node.val)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)
            ans.append(temp)
        return ans
            
