/*
// Definition for a Node.
class Node {
    public int val;
    public Node prev;
    public Node next;
    public Node child;
};
*/

class Solution {
    public Node flatten(Node head) {
        if (head == null) {
            return null;
        }

        if (head.child == null) {
            head.next = flatten(head.next);
            return head;
        }

        if (head.next == null) {
            head.next = flatten(head.child);
            head.child = null;
            head.next.prev = head;
            
            return head;
        }

        Node holder = head.next;
        head.next = flatten(head.child);
        head.next.prev = head;
        head.child = null;

        Node output = head;
        while (head.next != null) {
            head = head.next;
        } 
        head.next = flatten(holder);
        head.next.prev = head;

        return output;
    }
}