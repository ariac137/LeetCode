# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        MAX_LENGTH = 10 ** 4
        length = 0
        
        while head:
            head = head.next
            length += 1
            if length > MAX_LENGTH:
                return True
        
        return False