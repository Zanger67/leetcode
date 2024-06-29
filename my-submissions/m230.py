# In order traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.output = -1
        self.counter = 0
        return self.helper(root, k)

    def helper(self, curr: Optional[TreeNode], k: int) -> int : 
        if not curr :
            return 0

        temp = self.helper(curr.left, k)
        if temp :
            return temp

        self.counter += 1
        if self.counter == k :
            return curr.val

        return self.helper(curr.right, k)

