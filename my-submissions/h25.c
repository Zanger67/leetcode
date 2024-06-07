// https://leetcode.com/problems/reverse-nodes-in-k-group/description/

/* LET'S GOOOOOO 19 minutes using C hehe
 * Algo is O(n) runtime and O(n) space complexity
 * 
 * Will do the followup to get the O(1) space in a bit too :D
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode* currentGroup[k];

    struct ListNode* current = head;
    for (int i = 0; i < k; i++) {
        if (!current) {
            return head; // don't reverse this portion since not enough vals
        }

        currentGroup[k - i - 1] = current;
        current = current->next;
    }

    struct ListNode* nextGroup = currentGroup[0]->next;
    for (int i = 0; i < k - 1; i++) {
        currentGroup[i]->next = currentGroup[i + 1];
    }

    currentGroup[k - 1]->next = reverseKGroup(nextGroup, k);
    return currentGroup[0];

}