# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        vals = []

        def firstPass(curr: Optional[TreeNode], level: int) -> None :
            if curr.left :
                firstPass(curr.left, level + 1)

            if level % 2 :
                vals.append(curr.val)

            if curr.left :
                firstPass(curr.right, level + 1)

        def secondPass(curr: Optional[TreeNode], level: int) -> None :
            if curr.left :
                secondPass(curr.left, level + 1)

            if level % 2 :
                curr.val = vals.pop()

            if curr.left :
                secondPass(curr.right, level + 1)


        firstPass(root, 0)
        secondPass(root, 0)

        return root