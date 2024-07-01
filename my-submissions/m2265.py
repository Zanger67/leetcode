# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def helper(curr: TreeNode) -> [] : # summ, nodeCount, currSum
            if not curr :
                return [0, 0, 0]
            if not curr.left and not curr.right :
                return [curr.val, 1, 1]

            left = helper(curr.left)
            right = helper(curr.right)

            avg = (left[0] + right[0] + curr.val) // (left[1] + right[1] + 1)
            output = [left[x] + right[x] for x in range(3)]

            if curr.val == avg :
                output[2] += 1

            output[0] += curr.val
            output[1] += 1
            return output

        return helper(root)[2]