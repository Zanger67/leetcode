/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteNodes(struct ListNode* head, int m, int n) {
    struct ListNode* current = head;

    for (int i = 1; i < m && current; i++) {
        current = current->next;
    }

    while (current) {
        for (int j = 0; j < n && current->next; j++) {
            struct ListNode* temp = current->next;
            current->next = current->next->next;
            free(temp); // Freeing the values since they're now deleted
        }

        for (int i = 0; i < m && current; i++) {
            current = current->next;
        }
    }

    return head;
}