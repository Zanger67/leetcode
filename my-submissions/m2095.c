// Took ~1.5 minutes --> did it right after the java vers

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteMiddle(struct ListNode* head) {
    if (!head || !head->next) {
        return NULL;
    }

    struct ListNode* slow = head;
    struct ListNode* fast = head->next;

    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    slow->next = slow->next->next;
    
    return head;
    
}