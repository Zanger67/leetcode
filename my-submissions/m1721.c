// https://leetcode.com/problems/swapping-nodes-in-a-linked-list/description/

/* Took 3:05 total -- first attempt was in C and was quick despite that hehe
 * 97.79% runtime
 * 95.59% memory :D
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapNodes(struct ListNode* head, int k) {
    struct ListNode* left = head;

    for (int i = 1; i < k; i++) {
        left = left->next;
    }

    struct ListNode* rightSlow = head;
    struct ListNode* rightFast = head;

    for (int i = 0; i < k; i++) {
        rightFast = rightFast->next;
    }

    while (rightFast) {
        rightFast = rightFast->next;
        rightSlow = rightSlow->next;
    }

    int tempVal = left->val;
    left->val = rightSlow->val;
    rightSlow->val = tempVal;

    return head;
}