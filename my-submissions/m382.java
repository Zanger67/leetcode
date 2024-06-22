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
    private ListNode head;
    private int size;
    public Solution(ListNode head) {
        this.head = head;
        this.size = 0;

        ListNode curr = head;
        while (curr != null) {
            curr = curr.next;
            size++;
        }
    }
    
    public int getRandom() {
        int indx = (int) (Math.random() * size);
        ListNode curr = head;
        for (int i = 0; i < indx; i++) {
            curr = curr.next;
        }

        return curr.val;
    }
}

/**
 * Your Solution object will be instantiated and called as such:
 * Solution obj = new Solution(head);
 * int param_1 = obj.getRandom();
 */