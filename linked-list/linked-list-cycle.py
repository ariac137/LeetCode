# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
    
        # Use a set for O(1) lookups
        visited_nodes = set()
        
        curr = head
        while curr:
            # We store the node object itself (Python handles the id/hashing)
            if curr in visited_nodes:
                return True
            
            visited_nodes.add(curr)
            curr = curr.next
            
        return False