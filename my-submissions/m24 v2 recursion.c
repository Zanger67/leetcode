// https://leetcode.com/problems/swap-nodes-in-pairs/description/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* swapPairs(struct ListNode* head) {
    if (!head || !head->next) {
        return head;
    }

    // Swap of list[0] and list[1]
    struct ListNode* outputHead = head->next;
    head->next = swapPairs(outputHead->next); // Recurse for next 2
    outputHead->next = head;

    return outputHead;
}