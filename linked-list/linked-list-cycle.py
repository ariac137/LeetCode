# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        slow = head
        fast = head
        
        # We check fast and fast.next to ensure we can move 2 steps forward
        while fast and fast.next:
            slow = slow.next          # 1 step
            fast = fast.next.next     # 2 steps
            
            # If they meet, there's a loop!
            if slow == fast:
                return True
                
        # If fast hits the end, there is no loop
        return False