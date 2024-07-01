# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        self.counter = 0
        def helper(curr: TreeNode) -> (int, int) : # summ, nodeCount
            if not curr :
                return (0, 0)

            print(curr.val)
            if not curr.left and not curr.right :
                self.counter += 1
                return (curr.val, 1)

            left = helper(curr.left)
            right = helper(curr.right)

            output = (left[0] + right[0] + curr.val, left[1] + right[1] + 1)

            if curr.val == output[0] // output[1] :
                self.counter += 1
            return output
        
        helper(root)
        return self.counter