# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        mini = -math.inf
        maxi = math.inf
        dq = deque([(root, mini, maxi)])
        
        while dq:
            for i in range(len(dq)):
                node, tmin, tmax = dq.popleft()
                if not tmin < node.val < tmax: return False

                if node.left:
                    dq.append((node.left, tmin, node.val))
                if node.right:
                    dq.append((node.right, node.val, tmax))
                
        return True