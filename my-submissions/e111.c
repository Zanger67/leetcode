// https://leetcode.com/problems/minimum-depth-of-binary-tree/

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int min(int a, int b) {
    return (a < b) ? a : b;
}

int minDepthHelper(struct TreeNode* current) {
    if (!current->left && !current->right) 
        return 1;
    if (!current->left)
        return 1 + minDepthHelper(current->right);
    if (!current->right)
        return 1 + minDepthHelper(current->left);

    return 1 + min(minDepthHelper(current->left), minDepthHelper(current->right));
}
int minDepth(struct TreeNode* root) {
    if (!root)
        return 0;
    return minDepthHelper(root);
}

