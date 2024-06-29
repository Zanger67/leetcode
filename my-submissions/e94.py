# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.output = []
        def helper(curr: Optional[TreeNode]) -> None :
            if not curr :
                return
            
            helper(curr.left)
            self.output.append(curr.val)
            helper(curr.right)

        helper(root)
        return self.output