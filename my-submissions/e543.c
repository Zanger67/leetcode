/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int findHeight(struct TreeNode* node, int* diam) {
    if (!node) {
        return 0;
    }

    int hLeft = findHeight(node->left, diam);
    int hRight = findHeight(node->right, diam);

    if (hLeft + hRight > *diam) {
        *diam = hLeft + hRight;
    }

    return (((hLeft > hRight) ? hLeft : hRight) + 1);
} 

int diameterOfBinaryTree(struct TreeNode* root) {
    int* temp = (int*) malloc(sizeof(int));
    findHeight(root, temp);
    return *temp;
    free(temp);
}