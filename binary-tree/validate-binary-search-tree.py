# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        if not root.left and not root.right:
            return True
        
        if root.left and max(self.treeToList(root.left)) >= root.val:
            return False
        
        if root.right and min(self.treeToList(root.right)) <= root.val:
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
    

    def treeToList(self, root: Optional[TreeNode]) -> list:
        if not root:
            return []
        left = right = []
        if root.left:
            left = self.treeToList(root.left)
        if root.right:
            right = self.treeToList(root.right)

        return left + [root.val] + right
        
        
                
                

                