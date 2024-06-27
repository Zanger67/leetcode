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
    public ListNode reverseList(ListNode head) {
        head = helper(null, head);
        return head;
    }
    private ListNode helper(ListNode prev, ListNode curr) {
        if (curr == null) {
            return prev;
        }
        ListNode output = helper(curr, curr.next);
        curr.next = prev;
        return output; 
    }
}