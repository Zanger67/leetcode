# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def splitBST(self, root: Optional[TreeNode], target: int) -> List[Optional[TreeNode]]:
        if not root :
            return [None, None]

        if root.val == target :
            temp = root.right
            root.right = None
            return [root, temp]

        if root.val > target :
            temp = self.splitBST(root.left, target)
            root.left = temp[1]
            return [temp[0], root]

        temp = self.splitBST(root.right, target)
        root.right = temp[0]
        return [root, temp[1]]