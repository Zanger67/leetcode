/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

int doubleItHelper(struct ListNode* curr) {
    curr->val *= 2;
    if (curr->next) {
        curr->val += doubleItHelper(curr->next);
    }
    int carry = curr->val / 10;
    curr->val %= 10;
    return carry;
}

struct ListNode* doubleIt(struct ListNode* head){
    int carry = doubleItHelper(head);
    if (carry) {
        struct ListNode* newHead = (struct ListNode*) malloc(sizeof(struct ListNode));
        newHead->val = carry;
        newHead->next = head;
        return newHead;
    }
    return head;
}