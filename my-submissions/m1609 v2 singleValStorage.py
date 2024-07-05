# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        vals = []

        def dfs(curr: Optional[TreeNode], lvl: int = 0) -> bool :
            if not curr :
                return True

            if curr.val % 2 == lvl % 2 :
                return False
            
            if len(vals) <= lvl :
                vals.append(curr.val)
            elif vals[lvl] and ((lvl % 2 == 0 and vals[lvl] >= curr.val) or \
                                (lvl % 2 == 1 and vals[lvl] <= curr.val)) :
                return False
            else :
                vals[lvl] = curr.val
            
            lvl += 1
            return dfs(curr.left, lvl) and dfs(curr.right, lvl)
            
        return dfs(root)
