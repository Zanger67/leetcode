# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode]) -> (int, int) : # (sum, height)
            if not curr.left and not curr.right:
                return (curr.val, 1)
            if not curr.left :
                right = helper(curr.right)
                return (right[0], right[1] + 1)
            if not curr.right :
                left = helper(curr.left)
                return (left[0], left[1] + 1)

            left = helper(curr.left)
            right = helper(curr.right)

            if left[1] == right[1] :
                return (left[0] + right[0], left[1] + 1)
            if left[1] > right[1] :
                return (left[0], left[1] + 1)
            return (right[0], right[1] + 1)

        return helper(root)[0]