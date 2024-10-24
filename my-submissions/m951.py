# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def equiv(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool :
            if not left and not right :
                return True
            if not left or not right :
                return False
            if left.val != right.val :
                return False
            return (equiv(left.left, right.left) and equiv(left.right, right.right)) or \
                   (equiv(left.right, right.left) and equiv(left.left, right.right))
        return equiv(root1, root2)
