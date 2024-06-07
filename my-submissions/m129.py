# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.summ = 0

        def helper(current: Optional[TreeNode], currSum: []) -> None :
            if not current :
                print(int(''.join(currSum)))
                self.summ += int(''.join(currSum))
                return

            currSum.append(str(current.val))
            if current.left and current.right :
                helper(current.left, currSum)
                helper(current.right, currSum)
            elif current.left :
                helper(current.left, currSum)
            else :
                helper(current.right, currSum)

            currSum.pop()

        helper(root, [])
        return self.summ