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
    public void reorderList(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;

        while (fast.next != null && fast.next.next != null) {
            fast = fast.next.next;
            slow = slow.next;
        }

        ListNode prev = slow;
        slow = slow.next;
        prev.next = null;
        while (slow != null) {
            ListNode temp = slow.next;
            slow.next = prev;
            prev = slow;
            slow = temp;
        }

        ListNode front = head.next;
        ListNode back = prev;
        ListNode newHead = head;

        while (front != null && back != null) {
            if (back != null) {
                newHead.next = back;
                back = back.next;
                newHead = newHead.next;
            }

            if (front != null) {
                newHead.next = front;
                front = front.next;
                newHead = newHead.next;
            }
        }
        if (back != null) {
            newHead.next = back;
            back.next = null;
        }
    }
}