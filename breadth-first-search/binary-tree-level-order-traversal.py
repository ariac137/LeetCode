# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result
        
        tree = [root]
       
        while tree:
            temp_result = []
            
            for _ in range(len(tree)):
                node = tree.pop(0)
             
                temp_result.append(node.val)
                if node.left:
                    tree.append(node.left)
                    
                if node.right:
                    tree.append(node.right)
                   

            result.append(temp_result)
            
        return result

            
            
            
            
            
            
            
        