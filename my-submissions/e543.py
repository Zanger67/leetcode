# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # Return height but compare current diameter to maxCase
        # [height, maxDiameter]
        def maxCaseAndHeight(node: Optional[TreeNode]):
            if not node :
                return (0, 0)
            
            leftData = maxCaseAndHeight(node.left)
            rightData = maxCaseAndHeight(node.right)

            return (max(leftData[0], rightData[0]) + 1, # height
                    max(leftData[0] + rightData[0] + 1, # max diameter
                        leftData[1], 
                        rightData[1])
                    )

        # -1 cause PathNodes = PathEdges + 1
        return maxCaseAndHeight(root)[1] - 1

