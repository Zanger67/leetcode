# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumLevel(self, root: Optional[TreeNode]) -> int:
        levelSums = defaultdict(int)

        def dfs(curr: Optional[TreeNode], levelSums: defaultdict, lvl: int = 1) -> None :
            if not curr :
                return

            levelSums[lvl] += curr.val
            lvl += 1
            dfs(curr.left, levelSums, lvl)
            dfs(curr.right, levelSums, lvl)
        
        dfs(root, levelSums)
        return min(levelSums, key=lambda x: levelSums[x])