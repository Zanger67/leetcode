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
    TreeNode* bstFromPreorder(vector<int>& preorder) {
        TreeNode* root = new TreeNode(preorder[0]);
        bstHelper(preorder, root, 1, INT_MIN, INT_MAX);
        return root;
    }

    int bstHelper(vector<int>& preorder, TreeNode* curr, int indx, int lowerbound, int upperbound) {
        if (indx >= preorder.size()) {
            return indx;
        }
        
        if (lowerbound < preorder[indx] && preorder[indx] < curr->val) {
            curr->left = new TreeNode(preorder[indx]);
            indx = bstHelper(preorder, curr->left, indx + 1, lowerbound, curr->val);
        }

        if (indx >= preorder.size()) {
            return indx;
        }

        if (preorder[indx] < upperbound && preorder[indx] > curr->val) {
            curr->right = new TreeNode(preorder[indx]);
            indx = bstHelper(preorder, curr->right, indx + 1, curr->val, upperbound);
        }
        

        return indx;
    }
};