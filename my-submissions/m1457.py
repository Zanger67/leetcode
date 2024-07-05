# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(curr: Optional[TreeNode], vals: List[bool] = [False] * 10) -> int :
            if not curr :
                return 0
            
            vals[curr.val] = not vals[curr.val]

            if not curr.left and not curr.right :
                oddCnt = vals.count(True)
                vals[curr.val] = not vals[curr.val]
                if oddCnt <= 1 :
                    return 1
                return 0
            
            output = dfs(curr.left) + dfs(curr.right)
            vals[curr.val] = not vals[curr.val]
            return output
        
        return dfs(root)