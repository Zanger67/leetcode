/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> output;
        rsvHelper(root, 0, &output);
        return output;
    }

    void rsvHelper(TreeNode* curr, int depth, vector<int>* output) {
        if (not curr)
            return;
        if (depth == output->size())
            output->push_back(curr->val);
        
        depth++;
        rsvHelper(curr->right, depth, output);
        rsvHelper(curr->left, depth, output);
    }
};