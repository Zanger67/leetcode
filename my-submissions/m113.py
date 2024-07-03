# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root :
            return []
        output = []

        def helper(curr: Optional[TreeNode], currSum: int, path: List[int]) -> None :
            if not curr :
                return

            currSum += curr.val
            path.append(curr.val)

            if currSum == targetSum and not curr.left and not curr.right :
                output.append(path.copy())
            
            if curr.left :
                helper(curr.left, currSum, path)
            if curr.right :
                helper(curr.right, currSum, path)

            path.pop()
        helper(root, 0, [])

        return output