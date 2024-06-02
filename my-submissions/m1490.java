// https://leetcode.com/problems/clone-n-ary-tree/description/

/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    
    public Node() {
        children = new ArrayList<Node>();
    }
    
    public Node(int _val) {
        val = _val;
        children = new ArrayList<Node>();
    }
    
    public Node(int _val,ArrayList<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    public Node cloneTree(Node root) {
        if (root == null) {
            return null;
        }

        ArrayList<Node> newChildren = new ArrayList<>();
        for (Node i: root.children) {
            newChildren.add(cloneTree(i));
        }

        return new Node(root.val, newChildren);
    }
}