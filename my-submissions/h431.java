/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

class Codec {
    // Encodes an n-ary tree to a binary tree.
    public TreeNode encode(Node root) {
        if (root == null) {
            return null;
        }

        TreeNode newRoot = new TreeNode(root.val);
        TreeNode prev = null;

        for (Node child : root.children) {
            TreeNode replacement = encode(child);
            if (newRoot.left == null) {
                newRoot.left = replacement;
            } else {
                prev.right = replacement;
            }
            prev = replacement;
        }

        return newRoot;
    }
	
    // Decodes your binary tree to an n-ary tree.
    public Node decode(TreeNode root) {
        if (root == null) {
            return null;
        }

        Node output = new Node(root.val);
        TreeNode child = root.left;

        ArrayList<Node> children = new ArrayList<>();
        while (child != null) {
            children.add(decode(child));
            child = child.right;
        }

        output.children = children;
        return output;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.decode(codec.encode(root));