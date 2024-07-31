# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        counterpartVals = set()

        def dfs(curr: Optional[TreeNode]) -> bool :
            if not curr :
                return False
            if curr.val in counterpartVals :
                return True
            counterpartVals.add(k - curr.val)
            return dfs(curr.left) or dfs(curr.right)
        
        return dfs(root)