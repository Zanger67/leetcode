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
    public List<Integer> inorderTraversal(TreeNode root) {
        ArrayList<Integer> output = new ArrayList<>();
        helper(root, output);
        return output;
    }

    private void helper(TreeNode curr, ArrayList<Integer> output) {
        if (curr == null) {
            return;
        }
        helper(curr.left, output);
        output.add(curr.val);
        helper(curr.right, output);
    }
}