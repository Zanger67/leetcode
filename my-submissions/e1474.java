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
    public ListNode deleteNodes(ListNode head, int m, int n) {
        ListNode current = new ListNode(0);
        current.next = head;
        ListNode output = current;

        while (current != null) {
            for (int i = 0; i < m && current != null; i++) {
                current = current.next;
            }

            if (current == null) {
                break;
            }

            for (int j = 0; j < n && current.next != null; j++) {
                current.next = current.next.next;
            }
        }

        return output.next;
    }
}