# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        latestNode = root
        toVisit = [None]
        while latestNode :
            if latestNode.right :
                toVisit.append(latestNode.right)
            if latestNode.left :
                toVisit.append(latestNode.left)
                latestNode.left = None

            latestNode.right = toVisit.pop()
            latestNode = latestNode.right
