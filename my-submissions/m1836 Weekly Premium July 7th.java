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
    public ListNode deleteDuplicatesUnsorted(ListNode head) {
        HashMap<Integer, Integer> counts = new HashMap<>();
        
        ListNode curr = head;
        while (curr != null) {
            counts.put(curr.val, counts.getOrDefault(curr.val, 0) + 1);
            curr = curr.next;
        }

        ListNode dummy = new ListNode(0, head);
        ListNode output = dummy;

        while (dummy != null) {
            while (dummy.next != null && counts.get(dummy.next.val) > 1) {
                dummy.next = dummy.next.next;
            }
            dummy = dummy.next;
        }
        return output.next;
    }
}