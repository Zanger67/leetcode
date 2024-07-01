// Simpler O(1) solution with a lottttt less if statements lol

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */


void flatten(struct TreeNode* root) {
    struct TreeNode* current = root;

    bool onlyRightMovements = true;
    while (current) {
        if (current->left) {
            struct TreeNode* temp = current->left;
            while (temp->right) {
                temp = temp->right;
            }
            temp->right = current->right;
            current->right = current->left;
            current->left = NULL;
        } else {
            current = current->right;
        }
    }
}