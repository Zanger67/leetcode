// https://leetcode.com/problems/diameter-of-binary-tree/description/


/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int diameterOfBinaryTree(TreeNode root) {
        return helper(root)[1] - 1;
    }

    public int[] helper(TreeNode node) {
        if (node == null) {
            return new int[]{0, 0};
        }

        int[] leftData = helper(node.left);
        int[] rightData = helper(node.right);

        return new int[]{Integer.max(leftData[0], rightData[0]) + 1,
                         Integer.max(Integer.max(leftData[1], rightData[1]), leftData[0] + rightData[0] + 1)};

    }

    
}