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
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> output = new LinkedList<>();
        helper(root, 0, output);
        return output;
    }

    private void helper(TreeNode curr, int depth, List<List<Integer>> output) {
        if (curr == null) {
            return;
        }
        if (output.size() <= depth) {
            output.add(new LinkedList<Integer>());
        }
        output.get(depth).add(curr.val);

        depth++;
        if (curr.left != null) {
            helper(curr.left, depth, output);
        }
        if (curr.right != null) {
            helper(curr.right, depth, output);
        }
    }
}