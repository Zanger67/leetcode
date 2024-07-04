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
    public int minDepth(TreeNode root) {
        if (root == null) {
            return 0;
        }
        return minDepth(root, 1);
    }
    private int minDepth(TreeNode curr, int depth) {
        if (curr.left == null && curr.right == null) {
            return depth;
        }

        depth++;
        if (curr.left != null && curr.right != null) {
            return Integer.min(minDepth(curr.left, depth), minDepth(curr.right, depth));
        }

        if (curr.left != null) {
            return minDepth(curr.left, depth);
        }
        return minDepth(curr.right, depth);
    }
}