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
    struct ListNode* headPointer = head->next; // Store output head
    head->next = head->next->next;
    headPointer->next = head;

    // Starting reference nodes list[1], list[2]
    struct ListNode* pointerL = head;
    struct ListNode* pointerR = head->next;

    while (pointerR && pointerR->next) {
        pointerL->next = pointerR->next;
        pointerR->next = pointerR->next->next;

        pointerL->next->next = pointerR;

        // Reference nodes are now list[L+2], list[R+2] i.e. shift right by 2
        pointerL = pointerL->next->next;
        pointerR = pointerR->next;
    }

    return headPointer;
}