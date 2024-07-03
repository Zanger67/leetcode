# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root :
            return 0
        self.output = 0

        # Sums dict is a counter
        def dfs(curr: Optional[TreeNode], currSum: int) -> Counter :
            valNeeded = currSum + targetSum
            currSum += curr.val
            
            output = Counter()
            if curr.left :
                output += dfs(curr.left, currSum)
            if curr.right :
                output += dfs(curr.right, currSum)
            output[currSum] += 1

            self.output += output.get(valNeeded, 0)

            return output
        
        dfs(root, 0)
        return self.output