# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        temp = head
        while temp != None:
            temp = temp.next
            length += 1
        
        new_n = length - n
        if new_n == 0:
            return head.next
        
        temp = head
        while new_n != 1:
            temp = temp.next
            new_n -= 1
        
        temp.next = temp.next.next
        
        return head
        
        
        