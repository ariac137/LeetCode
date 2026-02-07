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
        prev_count = 1
        while tree:
            temp_result = []
            new_count = 0
            while prev_count > 0:
                node = tree.pop(0)
                prev_count -= 1
                temp_result.append(node.val)
                if node.left:
                    tree.append(node.left)
                    new_count += 1
                if node.right:
                    tree.append(node.right)
                    new_count += 1
            prev_count = new_count
            result.append(temp_result)
            
        return result

            
            
            
            
            
            
            
        