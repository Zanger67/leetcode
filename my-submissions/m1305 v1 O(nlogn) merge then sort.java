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
    private List<Integer> output;
    private void helper(TreeNode curr) {
        if (curr == null) 
            return;
        
        output.add(curr.val);
        helper(curr.left);
        helper(curr.right);
    }
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        output = new ArrayList<>();
        helper(root1);
        helper(root2);
        Collections.sort(output);
        
        return output;
    }
}