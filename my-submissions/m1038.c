/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int adjustNodeValues(struct TreeNode* root, int addVal) {
    int add = root->val + addVal;
    if (root->right) {
        add += adjustNodeValues(root->right, addVal) - addVal;
    }

    root->val = add;

    if (root->left) {
        add += adjustNodeValues(root->left, add) - add;
    }

    return add;
}

struct TreeNode* bstToGst(struct TreeNode* root) {
    adjustNodeValues(root, 0);
    return root;
}