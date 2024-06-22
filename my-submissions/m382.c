/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */



typedef struct {
    struct ListNode* head;
    int size;
} Solution;


Solution* solutionCreate(struct ListNode* head) {
    int size = 0;
    struct ListNode* curr = head;
    while (curr) {
        curr = curr->next;
        size++;
    }

    Solution* output = (struct Solution*) malloc(sizeof(Solution));
    output->size = size;
    output->head = head;

    return output;
}

int solutionGetRandom(Solution* obj) {
    int indx = rand() % (obj->size);

    struct ListNode* curr = obj->head;
    for (int i = 0; i < indx; i++) {
        curr = curr->next;
    }

    return curr->val;

}


// I'm presuming that we don't need to free the linkedlist
// Since that was fed initially as an outside obj
void solutionFree(Solution* obj) {
    free(obj);
}

/**
 * Your Solution struct will be instantiated and called as such:
 * Solution* obj = solutionCreate(head);
 * int param_1 = solutionGetRandom(obj);
 
 * solutionFree(obj);
*/