# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        # return (independent longest, longest of same value as src)
        def dfs(curr: Optional[TreeNode], prevVal: int) -> Tuple[int, int] :
            if not curr :
                return (0, 0)

            l, r = dfs(curr.left, curr.val), dfs(curr.right, curr.val)
            if curr.val != prevVal :
                b = 0
            else :
                b = 1 + max(l[1], r[1])

            return (max(l[1] + r[1] + 1, l[0], r[0]), b)
        
        return max(max(dfs(root, -9999)) - 1, 0)