# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        def dfs(curr: Optional[TreeNode], count: list) -> int : # net dif of coins
            if not curr :
                return 0

            if curr.left :
                curr.val += dfs(curr.left, count)
            if curr.right :
                curr.val += dfs(curr.right, count)

            coinDif = curr.val - 1
            count[0] += abs(coinDif)
            return coinDif

        count = [0]
        dfs(root, count)
        return count[0]
