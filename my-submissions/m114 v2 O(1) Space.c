// O(1) space let's gooooo

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

// I'm gonna try this with O(1) space 
/** Plan:
  * Iterate to the very leftmost node
  * Set the previous node's right to the leftmost and the leftmost's next to the previous right
  * repeat iterating upwards (iterate through the new right branch first)
  */


void flatten(struct TreeNode* root) {
    struct TreeNode* current = root;

    bool onlyRightMovements = true;
    while (current) {
        if (!(current->left) && !(current->right)) {
            if (onlyRightMovements) {
                return;
            } else {
                onlyRightMovements = true;
                current = root;
            }
        } else if (current->left) {
            if (!(current->left->right)) { // next left is leaf
                current->left->right = current->right;
                current->right = current->left;
                current->left = NULL;
                current = current->right;
            } else if (!(current->left->left)) {
                current->left->left = current->left->right;
                current->left->right = NULL;
            } else {
                current = current->left;
                onlyRightMovements = false;
            }
        } else { // only right branch exists
            current = current->right;
        }
    }
}