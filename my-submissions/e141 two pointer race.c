// https://leetcode.com/problems/linked-list-cycle/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
bool hasCycle(struct ListNode *head) {
    // Since no dynamic space and I don't feel like implementing a full datastructure,
    // let's do a 2-pointer method

    if (!head || !head->next) {
        return false;
    }

    struct ListNode *one = head;
    struct ListNode *two = head->next;

    while (one != two) {
        if (!two->next || !two->next->next) {
            return false;
        }
        one = one->next;
        two = two->next->next;
    }

    return true;
    
}