# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root :
            return False

        def dfs(curr: Optional[TreeNode], remaining: int) -> bool :
            if not curr :
                return remaining == 0
        
            remaining -= curr.val
            if curr.left and curr.right :
                return dfs(curr.left, remaining) or \
                       dfs(curr.right, remaining)
            if curr.left :
                return dfs(curr.left, remaining)
            return dfs(curr.right, remaining)
        
        return dfs(root, targetSum)