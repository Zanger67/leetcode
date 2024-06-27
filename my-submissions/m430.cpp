/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* prev;
    Node* next;
    Node* child;
};
*/

class Solution {
public:
    Node* flatten(Node* head) {
        if (!head) {
            return NULL;
        }

        if (!head->child) {
            head->next = flatten(head->next);
            return head;
        }

        if (!head->next) {
            head->next = flatten(head->child);
            head->child = NULL;
            head->next->prev = head;
            return head;
        }

        Node* holder = head->next;
        head->next = flatten(head->child);
        head->next->prev = head;
        head->child = NULL;

        Node* output = head;

        while (head->next) {
            head = head->next;
        }

        head->next = flatten(holder);
        head->next->prev = head;

        return output;
    }
};
