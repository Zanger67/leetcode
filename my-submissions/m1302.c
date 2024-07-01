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

int* helper(struct TreeNode* current) {
    if (!current->left && !current->right) {
        int* output = (int*) malloc(sizeof(int) * 2);
        output[0] = current->val;
        output[1] = 1;
        return output;
    }

    if (!current->left) {
        int* right = helper(current->right);
        right[1] += 1;
        return right;
    }

    if (!current->right) {
        int* left = helper(current->left);
        left[1] += 1;
        return left;
    }

    int* left = helper(current->left);
    int* right = helper(current->right);

    if (left[1] == right[1]) {
        left[0] += right[0];
        left[1] += 1;
        free(right);
        return left;
    } else if (left[1] > right[1]) {
        free(right);
        left[1] += 1;
        return left;
    } else {
        free(left);
        right[1] += 1;
        return right;
    }
}

int deepestLeavesSum(struct TreeNode* root) {
    int* output = helper(root);
    int out = output[0];
    free(output);
    return out;
}