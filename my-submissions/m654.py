# https://leetcode.com/problems/maximum-binary-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0 :
            return None
        maxx = max(nums)
        
        return TreeNode(maxx, 
                        self.constructMaximumBinaryTree(nums[:nums.index(maxx)]), 
                        self.constructMaximumBinaryTree(nums[nums.index(maxx) + 1:]))