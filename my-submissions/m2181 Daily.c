/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* mergeNodes(struct ListNode* head) {
    struct ListNode* curr = head;
    while (curr->next) {
        if (curr->next->val == 0) {
            if (!curr->next->next) {
                curr->next = NULL;
                break;
            }
            curr = curr->next;
        } else {
            curr->val += curr->next->val;
            curr->next = curr->next->next;
        }
    }

    return head;
}