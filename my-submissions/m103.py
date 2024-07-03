#
# @lc app=leetcode id=103 lang=python3
#
# [103] Binary Tree Zigzag Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        toVisit = deque([root])
        leftRight = True
        output = []

        while toVisit :
            width = len(toVisit)
            lvl = []
            for i in range(width):
                if leftRight :
                    curr = toVisit.popleft()
                    lvl.append(curr.val)
                    if curr.left :
                        toVisit.append(curr.left)
                    if curr.right :
                        toVisit.append(curr.right)
                else :
                    curr = toVisit.pop()
                    lvl.append(curr.val)
                    if curr.right :
                        toVisit.appendleft(curr.right)
                    if curr.left :
                        toVisit.appendleft(curr.left)

            output.append(lvl)
            leftRight = not leftRight
        return output
        
# @lc code=end

