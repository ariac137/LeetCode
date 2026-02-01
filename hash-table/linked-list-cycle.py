# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
            
        existing_address = []
        MAX_COUNT = 10 ** 4
        count = 0
        while head:
            if id(head) in existing_address:
                return True
            existing_address.append(id(head))
            count += 1
            if count > MAX_COUNT:
                return True
            head = head.next
        
        return False