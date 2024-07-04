# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root :
            if (root == p) or (root == q) :
                break
            if (root.val < p.val) == (root.val > q.val) :
                break
            if root.val < p.val :
                root = root.right
            else :
                root = root.left
        return root