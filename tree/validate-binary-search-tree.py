# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        vals = []
        
        def inOrder(node):
            if not node:
                return
            inOrder(node.left)
            vals.append(node.val)
            inOrder(node.right)
            
        inOrder(root)
        
        # Check if the list is strictly increasing
        for i in range(1, len(vals)):
            if vals[i] <= vals[i-1]:
                return False
        return True