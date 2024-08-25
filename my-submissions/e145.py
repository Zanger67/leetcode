# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        def dfs(curr: Optional[TreeNode], output: List[int] = []) -> List[int] :
            if not curr :
                return output
            if curr.left :
                dfs(curr.left, output)
            if curr.right :
                dfs(curr.right, output)
            output.append(curr.val)
            return output
        return dfs(root)
