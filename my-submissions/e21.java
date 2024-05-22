// https://leetcode.com/problems/merge-two-sorted-lists/description/

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
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        if (list1 == null && list2 == null) {
            return null;
        }

        if (list1 == null && list2 != null) {
            return new ListNode(list2.val, mergeTwoLists(null, list2.next));
        } else if (list1 != null && list2 == null) {
            return new ListNode(list1.val, mergeTwoLists(list1.next, null));
        } else {
            if (list1.val < list2.val) {
                return new ListNode(list1.val, mergeTwoLists(list1.next, list2));
            } else {
                return new ListNode(list2.val, mergeTwoLists(list1, list2.next));
            }
        }

    }
}