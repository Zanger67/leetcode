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
    public List<Integer> rightSideView(TreeNode root) {
        List<Integer> output = new LinkedList<>();
        rsvHelper(root, 0, output);
        return output;
    }

    private void rsvHelper(TreeNode curr, int depth, List<Integer> output) {
        if (curr == null) {
            return;
        }
        if (depth == output.size()) {
            output.add(curr.val);
        }

        depth++;
        rsvHelper(curr.right, depth, output);
        rsvHelper(curr.left, depth, output);
    }
}