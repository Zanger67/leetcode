# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(curr: Optional[TreeNode], low: int, high: int) -> int :
            output = 0

            if not curr :
                return output

            if low <= curr.val <= high :
                output += curr.val + dfs(curr.left, low, high) + dfs(curr.right, low, high)
            elif curr.val < low : 
                output += dfs(curr.right, low, high)
            else :
                output += dfs(curr.left, low, high)
            return output
        return dfs(root, low, high)