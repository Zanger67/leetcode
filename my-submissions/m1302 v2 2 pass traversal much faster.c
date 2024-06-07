// Not that efficient :l
// probs cause of all the mallocing

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */
int max(int a, int b) {
    return (a > b) ? a : b;
}

int findDepth(struct TreeNode* current) {
    if (!current) 
        return 0;
    return 1 + max(findDepth(current->left), findDepth(current->right));
}

int sumDeepest(struct TreeNode* current, int targetDepth, int currDepth) {
    if (!current)
        return 0;
    if (currDepth == targetDepth)
        return current->val;
    
    return sumDeepest(current->left, targetDepth, currDepth + 1) + 
           sumDeepest(current->right, targetDepth, currDepth + 1);
}

int deepestLeavesSum(struct TreeNode* root) {
    return sumDeepest(root, findDepth(root), 1);
}