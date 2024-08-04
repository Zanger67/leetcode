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
    public String tree2str(TreeNode root) {
        return helper(root, new StringBuilder()).toString();
    }

    public StringBuilder helper(TreeNode curr, StringBuilder sb) {
        sb.append(curr.val);

        if (curr.left != null) {
            sb.append("(");
            helper(curr.left, sb);
            sb.append(")");
        } else if (curr.right != null) {
            sb.append("()");
        }
        if (curr.right != null) {
            sb.append("(");
            helper(curr.right, sb);
            sb.append(")");
        }
        return sb;
    }
}