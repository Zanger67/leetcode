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
    public TreeNode findNearestRightNode(TreeNode root, TreeNode u) {
        Queue<Integer> depths = new LinkedList<>();
        Queue<TreeNode> nodes = new LinkedList<>();
        nodes.add(root);
        depths.add(1);

        while (!depths.isEmpty()) {
            TreeNode curr = nodes.remove();
            int depth = depths.remove();

            if (curr == u) {
                if (depths.isEmpty()) {
                    return null;
                }
                if (depths.remove() == depth) {
                    return nodes.remove();
                }
                return null;
            }

            if (curr.left != null) {
                nodes.add(curr.left);
                depths.add(depth + 1);
            }
            if (curr.right != null) {
                nodes.add(curr.right);
                depths.add(depth + 1);
            }
        }
        return null;
    }
}