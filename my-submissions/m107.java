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
    public List<List<Integer>> levelOrderBottom(TreeNode root) {
        HashMap<Integer, List<Integer>> levelOrderVals = new HashMap<>();
        int maxDepth = helper(root, 0, levelOrderVals);

        List<List<Integer>> output = new LinkedList<>();
        for (int i = maxDepth; i >= 0; i--) {
            output.add(levelOrderVals.get(i));
        }

        return output;
    }

    private int helper(TreeNode curr, int depth, HashMap<Integer, List<Integer>> levelOrderVals) {
        if (curr == null) {
            return depth - 1;
        }
        if (!levelOrderVals.containsKey(depth)) {
            levelOrderVals.put(depth, new LinkedList<Integer>());
        }
        levelOrderVals.get(depth).add(curr.val);

        depth++;
        return Integer.max(helper(curr.left, depth, levelOrderVals), helper(curr.right, depth, levelOrderVals));
    }
}