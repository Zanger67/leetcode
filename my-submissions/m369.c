/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int plusOneHelper(struct ListNode* curr) {
    if (curr->next) {
        curr->val += plusOneHelper(curr->next);
    } else {
        curr->val++;
    }
    if (curr->val >= 10) {
        curr->val -= 10;
        return 1;
    }
    return 0;
}


struct ListNode* plusOne(struct ListNode* head){
    int carry = plusOneHelper(head);
    if (carry) {
        struct ListNode* newHead = (struct ListNode*) malloc(sizeof(struct ListNode));
        newHead->val = 1;
        newHead->next = head;
        return newHead;
    }
    return head;
}