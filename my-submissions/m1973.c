/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int output;

long helper(struct TreeNode* root) {
    if (!root) {
        return 0;
    }

    long sum = helper(root->left) + helper(root->right);

    if (root->val == sum) {
        output++;
    }

    return sum + root->val;
}


int equalToDescendants(struct TreeNode* root) {
    output = 0;
    helper(root);

    return output;
}