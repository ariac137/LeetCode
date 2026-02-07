# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left = root.left
        right = root.right
        
        if not left and not right:
            return True
        
        elif left and right:
            return self.mirrorTree(left, right)
            
        else:
            return False
    
    
    def mirrorTree(self, tree1: Optional[TreeNode], tree2: Optional[TreeNode]) -> bool:
        if not tree1 and not tree2:
            return True
        
        if (not tree1 and tree2) or (tree1 and not tree2):
            return False
        
        if tree1.val != tree2.val:
            return False
        
        left1 = tree1.left
        right1 = tree1.right
        
        left2 = tree2.left
        right2 = tree2.right
        
        return self.mirrorTree(left1, right2) and self.mirrorTree(left2, right1)