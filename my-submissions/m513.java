
import java.awt.Point;/**
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
    public int findBottomLeftValue(TreeNode root) {
        return helper(root, 0).x;
    }

    // Return (val, depth)
    private Point helper(TreeNode curr, int depth) {
        if (curr.left == null && curr.right == null) {
            return new Point(curr.val, depth);
        }

        depth++;
        if (curr.left != null && curr.right != null) {
            Point l = helper(curr.left, depth);
            Point r = helper(curr.right, depth);

            if (l.y < r.y) {
                return r;
            }
            return l;
        }

        if (curr.left != null) {
            return helper(curr.left, depth);
        }
        return helper(curr.right, depth);
    }
}