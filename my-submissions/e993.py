# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # schema: (depth, parent)
        ref = []

        def dfs(curr: Optional[TreeNode], prev: Optional[TreeNode], depth: int = 0) -> None :
            if not curr or len(ref) >= 2 :
                return
            
            if ref and depth > ref[0][0] :
                return

            if curr.val == x :
                ref.append((depth, prev))
            elif curr.val == y :
                ref.append((depth, prev))
            
            depth += 1
            dfs(curr.left, curr, depth)
            dfs(curr.right, curr, depth)
        
        dfs(root, None)

        if len(ref) < 2 :
            return False
        return ref[0][0] == ref[1][0] and ref[0][1] != ref[1][1]