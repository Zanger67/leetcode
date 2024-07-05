/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    vector<int> nodesBetweenCriticalPoints(ListNode* head) {
        vector<int> output;
        if (!head || !head->next || !head->next->next) {
            output.push_back(-1);
            output.push_back(-1);
            return output;
        }

        int earliestIndx = 0;
        int latestIndx = 0;
        int prevIndx = 0;
        int indx = 1;
        int prevprev = head->val;
        int prev = head->next->val;
        head = head->next->next;
        int minSpace = INT_MAX;

        while (head) {
            if ((prev > head->val && prev > prevprev) ||
                (prev < head->val && prev < prevprev)) {
                    if (!earliestIndx) {
                        earliestIndx = indx;
                    }
                    if (latestIndx && indx - latestIndx < minSpace) {
                        minSpace = indx - latestIndx;
                    }
                    latestIndx = indx;
                    
                }
            
            prevprev = prev;
            prev = head->val;
            head = head->next;
            indx++;
        }

        if (minSpace == INT_MAX) {
            output.push_back(-1);
            output.push_back(-1);
            return output;
        }

        output.push_back(minSpace);
        output.push_back(latestIndx - earliestIndx);
        return output;
    }
};