# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        curr = head
        while curr.next != None:
            next_node = curr.next
            temp_next_next = next_node.next
            next_node.next = head
            curr.next = temp_next_next
            head = next_node
            
        return head
            