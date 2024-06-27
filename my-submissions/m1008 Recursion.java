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
    public TreeNode bstFromPreorder(int[] preorder) {
        TreeNode root = new TreeNode(preorder[0]);
        bstHelper(preorder, root, 1, Integer.MIN_VALUE, Integer.MAX_VALUE);

        return root;
    }

    private int bstHelper(int[] preorder, TreeNode curr, int indx, int lowerbound, int upperbound) {
        if (indx >= preorder.length) {
            return indx;
        }

        if (lowerbound < preorder[indx] && preorder[indx] < curr.val) {
            curr.left = new TreeNode(preorder[indx]);
            indx = bstHelper(preorder, curr.left, indx + 1, lowerbound, curr.val);
        }
        
        if (indx >= preorder.length) {
            return indx;
        }
        
        if (preorder[indx] < upperbound && preorder[indx] > curr.val) {
            curr.right = new TreeNode(preorder[indx]);
            indx = bstHelper(preorder, curr.right, indx + 1, curr.val, upperbound);
        }

        return indx;
    }
}