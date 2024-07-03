"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""

class Codec:
    # Encodes an n-ary tree to a binary tree.
    def encode(self, root: 'Optional[Node]') -> Optional[TreeNode]:
        if not root :
            return None

        newRoot = TreeNode(root.val)

        # Same depth are right branch
        prev = None
        for child in root.children :
            treeReplacement = self.encode(child) # left branch encode children
            if not newRoot.left :
                newRoot.left = treeReplacement
            else :
                prev.right = treeReplacement
            prev = treeReplacement

        return newRoot


	# Decodes your binary tree to an n-ary tree.
    def decode(self, data: Optional[TreeNode]) -> 'Optional[Node]':
        if not data :
            return None


        outputNode = Node(data.val)
        outputNode.children = []

        # data.left,
        # data.left.right,
        # data.left.right.right,
        # data.left.right.right.right, etc. = children
        temp = data.left

        while temp :
            outputNode.children.append(self.decode(temp))
            temp = temp.right

        return outputNode
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(root))