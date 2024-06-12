# https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        check = []      # (node, parent val, grandparent val)
        outputSum = 0

        if root.left :
            check.append((root.left.left, root.left.val, root.val))
            check.append((root.left.right, root.left.val, root.val))

        if root.right :
            check.append((root.right.right, root.right.val, root.val))
            check.append((root.right.left, root.right.val, root.val))

        while check :
            curr, parentVal, grandParentVal = check.pop()
            if not curr :
                continue
            
            if grandParentVal % 2 == 0 :
                outputSum += curr.val
            
            check.append((curr.left, curr.val, parentVal))
            check.append((curr.right, curr.val, parentVal))

        return outputSum