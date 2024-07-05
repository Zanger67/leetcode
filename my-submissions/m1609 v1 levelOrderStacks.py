# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        vals = defaultdict(list)

        def dfs(curr: Optional[TreeNode], lvl: int = 0) -> bool :
            if not curr :
                return True
            if curr.val % 2 == lvl % 2 :
                return False
            if lvl in vals and ((lvl % 2 == 0 and vals[lvl][-1] >= curr.val) or \
                                (lvl % 2 == 1 and vals[lvl][-1] <= curr.val)) :
                return False
            
            vals[lvl].append(curr.val)
            
            lvl += 1
            return dfs(curr.left, lvl) and dfs(curr.right, lvl)
            
        return dfs(root)
