# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def helper(curr: Optional[TreeNode], minn: int, maxx: int) -> int :
            if not curr :
                return maxx - minn

            if curr.val < minn :
                minn = curr.val
            if curr.val > maxx :
                maxx = curr.val

            return max(maxx - minn, 
                        helper(curr.left, minn, maxx), 
                        helper(curr.right, minn, maxx))


        return helper(root, root.val, root.val)