# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        self.output:int = 0

        def infectDecendents(curr: Optional[TreeNode], time: int) -> None :
            self.output = max(self.output, time)

            time += 1
            if curr.left :
                infectDecendents(curr.left, time)
            if curr.right :
                infectDecendents(curr.right, time)

        def infectUpwards(curr: Optional[TreeNode]) -> int :
            if not curr :
                return 0

            if curr.val == start :
                if curr.left :
                    infectDecendents(curr.left, 1)
                if curr.right :
                    infectDecendents(curr.right, 1)
                return 1
            
            left = infectUpwards(curr.left)
            right = infectUpwards(curr.right)
            maxx = max(left, right)
            
            if maxx == 0 :
                return 0

            self.output = max(self.output, maxx)
            
            maxx += 1
            if left == 0 and curr.left :
                infectDecendents(curr.left, maxx)
            elif right == 0 and curr.right :
                infectDecendents(curr.right, maxx)
            
            return maxx

        infectUpwards(root)

        return self.output