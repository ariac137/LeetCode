/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0);  // Dummy node before head of sorted list
        ListNode curr = head;              // Current node to be inserted

        while (curr != null) {
            ListNode prev = dummy;         // Start at dummy every time
            ListNode next = curr.next;     // Save next node

            // Find where to insert curr
            while (prev.next != null && prev.next.val < curr.val) {
                prev = prev.next;
            }

            // Insert curr between prev and prev.next
            curr.next = prev.next;
            prev.next = curr;

            curr = next;
        }

        return dummy.next;
    }
        
}