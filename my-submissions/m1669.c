/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){

    struct ListNode* aMinusOne = list1;

    for (int i = 0; i < a - 1; i++) {
        aMinusOne = aMinusOne->next;
    }

    struct ListNode* bPlusOne = aMinusOne;

    for (int i = a - 1; i <= b; i++) {
        bPlusOne = bPlusOne->next;
    }

    aMinusOne->next = list2;

    while (aMinusOne->next) {
        aMinusOne = aMinusOne->next;
    }

    aMinusOne->next = bPlusOne;
    return list1;
}