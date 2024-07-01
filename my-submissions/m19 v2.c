/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* removeNthFromEnd(struct ListNode* head, int n) {
    if (!head || !head->next) {
        return NULL;
    }

    struct ListNode* left = head;
    struct ListNode* right = head;

    for (int i = 0; i < n; i++) {
        right = right->next;
    }

    if (!right) {
        return head->next;
    }

    while (right->next) {
        left = left->next;
        right = right->next;
    }

    left->next = left->next->next;

    return head;
}