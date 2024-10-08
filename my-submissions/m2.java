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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        if (l1 == null || l2 == null) {
            return null;
        }

        ListNode output = new ListNode();
        ListNode current = output;
        int carry = 0;
        while (l1 != null && l2 != null) {
            current.val = l1.val + l2.val + carry;
            carry = 0;
            if (current.val >= 10) {
                current.val -= 10;
                carry = 1;
            }


            if (l1.next == null || l2.next == null) {
                break;
            }

            current.next = new ListNode();
            current = current.next;
            l1 = l1.next;
            l2 = l2.next;
        }


        while (l1.next != null) {
            current.next = new ListNode();
            current = current.next;
            l1 = l1.next;


            current.val = l1.val + carry;
            carry = 0;
            if (current.val >= 10) {
                current.val -= 10;
                carry = 1;
            }

        }

        while (l2.next != null) {
            current.next = new ListNode();
            current = current.next;
            l2 = l2.next;
            
            current.val = l2.val + carry;
            carry = 0;
            if (current.val >= 10) {
                current.val -= 10;
                carry = 1;
            }

        }

        if (carry == 1) {
            current.next = new ListNode(1);
        }


        return output;
    }
}