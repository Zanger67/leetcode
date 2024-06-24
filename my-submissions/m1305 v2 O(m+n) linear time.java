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
    private void helper(TreeNode curr, Stack<Integer> stk) {
        if (curr == null) {
            return;
        }

        if (curr.right != null) {
            helper(curr.right, stk);
        }

        stk.add(curr.val);

        if (curr.left != null) {
            helper(curr.left, stk);
        }
    }
    
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        Stack<Integer> one = new Stack<>();
        Stack<Integer> two = new Stack<>();

        helper(root1, one);
        helper(root2, two);

        List<Integer> output = new LinkedList<>();

        while (!one.isEmpty() && !two.isEmpty()) {
            if (one.peek() < two.peek()) {
                output.add(one.pop());
            } else {
                output.add(two.pop());
            }
        }

        while (!one.isEmpty()) {
            output.add(one.pop());
        }

        while (!two.isEmpty()) {
            output.add(two.pop());
        }
        
        return output;
    }
}