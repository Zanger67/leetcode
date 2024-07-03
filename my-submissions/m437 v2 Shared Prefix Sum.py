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

        prefixSum = {}
        self.output = 0

        # Sums dict is a counter
        def dfs(curr: Optional[TreeNode], currSum: int) -> None :
            prefixSum[currSum] = prefixSum.get(currSum, 0) + 1
            valNeeded = currSum + curr.val - targetSum
            self.output += prefixSum.get(valNeeded, 0)

            if curr.left :
                dfs(curr.left, currSum + curr.val)
            if curr.right :
                dfs(curr.right, currSum + curr.val)

            prefixSum[currSum] -= 1

        dfs(root, 0)
        return self.output