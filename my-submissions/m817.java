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
    public int numComponents(ListNode head, int[] nums) {
        HashSet<Integer> ref = new HashSet<>();
        for (int i : nums) {
            ref.add(i);
        }

        int counter = 0;
        boolean previousIsComponent = false;
        while (head != null) {
            if (ref.contains(head.val)) {
                if (!previousIsComponent) {
                    counter++;
                }
                previousIsComponent = true;
            } else {
                previousIsComponent = false;
            }

            head = head.next;
        }
        return counter;
    }
}