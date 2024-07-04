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
    public int goodNodes(TreeNode root) {
        return goodNodesHelper(root, Integer.MIN_VALUE);
    }
    private int goodNodesHelper(TreeNode curr, int maxPrevious) {
        int output = (curr.val >= maxPrevious) ? 1 : 0;
        int maxx = Integer.max(curr.val, maxPrevious);
        if (curr.left != null) {
            output += goodNodesHelper(curr.left, maxx);
        }
        if (curr.right != null) {
            output += goodNodesHelper(curr.right, maxx);
        }
        return output;
    }
}