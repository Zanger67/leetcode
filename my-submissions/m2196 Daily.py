# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        children = set()
        nodes = {}

        for p, c, isleft in descriptions :
            nodes[p] = nodes.get(p, TreeNode(val=p))
            nodes[c] = nodes.get(c, TreeNode(val=c))

            if isleft :
                nodes[p].left = nodes[c]
            else :
                nodes[p].right = nodes[c]

            children.add(nodes[c])

        return list(set(nodes.values()) - children)[0]