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
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) {
            return new int[]{-1, -1};
        }

        ArrayList<Integer> critPts = new ArrayList<>();
        int indx = 0;
        int prevprev = head.val;
        int prev = head.next.val;
        head = head.next.next;

        int minSpace = Integer.MAX_VALUE;

        while (head != null) {
            if ((prev > head.val && prev > prevprev) ||
                (prev < head.val && prev < prevprev)) {
                    if (critPts.size() > 0 && indx - critPts.getLast() < minSpace) {
                        minSpace = indx - critPts.getLast();
                    }
                    critPts.add(indx);
                }
            prevprev = prev;
            prev = head.val;
            head = head.next;
            indx++;
        }

        if (critPts.size() < 2) {
            return new int[]{-1, -1};
        }

        return new int[]{minSpace, critPts.getLast() - critPts.get(0)};
    }
}