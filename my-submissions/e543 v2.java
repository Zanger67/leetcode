// https://leetcode.com/problems/diameter-of-binary-tree/submissions/1276753436/?envType=problem-list-v2&envId=r9zp3ka3

// Beats 100% 



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
    private int diam = Integer.MIN_VALUE;
    public int diameterOfBinaryTree(TreeNode root) {
        helper(root);
        return diam;
    }

    public int helper(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftData = helper(node.left);
        int rightData = helper(node.right);

        if (diam <= leftData + rightData) {
            diam = leftData + rightData;
        }

        return Integer.max(leftData, rightData) + 1;
    }

    
}