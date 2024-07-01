# Very fast (98%+) damn
# Stringification is niceeeeeee

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def getString(node: Optional[TreeNode]) -> str:
            if not node :
                return '_'
            
            return "-" + str(node.val) + "-" + getString(node.left) + getString(node.right)
        
        rootStr = getString(root)
        subStr = getString(subRoot)

        return subStr in rootStr