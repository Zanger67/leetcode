# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def dfs(curr: Optional[TreeNode]) -> Optional[TreeNode] :
            if not curr :
                return None

            if curr.left :
                curr.left = dfs(curr.left)
            if curr.right :
                curr.right = dfs(curr.right)

            if not curr.left and not curr.right and curr.val == target :
                return None

            return curr

        return dfs(root)
