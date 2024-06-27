/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     struct TreeNode *left;
 *     struct TreeNode *right;
 * };
 */

int bstHelper(int* preorder, int preorderSize, struct TreeNode* curr, int indx, int lowerbound, int upperbound) {
    if (indx >= preorderSize) {
        return indx;
    }
    
    if (lowerbound < preorder[indx] && preorder[indx] < curr->val) {
        curr->left = (struct TreeNode*) malloc(sizeof(struct TreeNode));
        curr->left->val = preorder[indx];
        curr->left->left = NULL;
        curr->left->right = NULL;
        indx = bstHelper(preorder, preorderSize, curr->left, indx + 1, lowerbound, curr->val);
    }

    if (indx >= preorderSize) {
        return indx;
    }
    
    if (preorder[indx] < upperbound && preorder[indx] > curr->val) {
        curr->right = (struct TreeNode*) malloc(sizeof(struct TreeNode));
        curr->right->val = preorder[indx];
        curr->right->right = NULL;
        curr->right->left = NULL;
        indx = bstHelper(preorder, preorderSize, curr->right, indx + 1, curr->val, upperbound);
    }

    return indx;
}

struct TreeNode* bstFromPreorder(int* preorder, int preorderSize) {
    struct TreeNode* root = (struct TreeNode*) malloc(sizeof(struct TreeNode));
    root->val = preorder[0];
    root->left = NULL;
    root->right = NULL;
    bstHelper(preorder, preorderSize, root, 1, INT_MIN, INT_MAX);
    return root;
}
