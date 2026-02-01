# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        
        head_list = []
        while head != None:
            head_list.append(head.val)
            head = head.next
        
        head_list.reverse()
        prev = None
        i = 0
        while i < len(head_list):
            if prev != None:
                prev.next = ListNode(head_list[i])
                prev = prev.next
            else:
                new_head = ListNode(head_list[i])
                prev = new_head
            i += 1
        return new_head