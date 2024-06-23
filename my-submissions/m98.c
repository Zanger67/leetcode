/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

bool isValidBSTHelper(struct TreeNode* root, long min, long max) {
    if (!root) 
        return true;

    if ((long) root->val <= min || (long) root->val >= max) 
        return false;

    bool output = true;
    
    if (root->right)
        output &= root->val < root->right->val
                    && isValidBSTHelper(root->right, (long) root->val, max);

    if (root->left)
        output &= root->left->val < root->val
                    && isValidBSTHelper(root->left, min, (long) root->val);

    return output;
}

bool isValidBST(struct TreeNode* root) {
    return isValidBSTHelper(root, LONG_MIN, LONG_MAX);
}