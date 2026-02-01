# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr = list1
                list1 = list1.next
            else:
                curr = list2
                list2 = list2.next
            head = curr
        elif list1 == None:
            return list2
        else:
            return list1

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next
            
        if list1 != None:
            curr.next = list1
        
        if list2 != None:
            curr.next = list2
            
        return head
                