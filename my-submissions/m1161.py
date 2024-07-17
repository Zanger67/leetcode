# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        lvls = defaultdict(int)

        def dfs(curr: Optional[TreeNode], lvls: defaultdict, lvl: int = 1) -> None :
            if not curr :
                return
            
            lvls[lvl] += curr.val

            dfs(curr.left, lvls, lvl + 1)
            dfs(curr.right, lvls, lvl + 1)

        dfs(root, lvls)
        return max(lvls.keys(), key=lambda x: lvls[x])