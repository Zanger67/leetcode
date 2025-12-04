# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        bst2 = set()
        nxt = [root2]
        while nxt :
            curr = nxt.pop()
            bst2.add(curr.val)
            if curr.left :
                nxt.append(curr.left)
            if curr.right :
                nxt.append(curr.right)
        
        nxt = [root1]
        while nxt :
            curr = nxt.pop()
            if target - curr.val in bst2 :
                return True
            
            if curr.left :
                nxt.append(curr.left)
            if curr.right :
                nxt.append(curr.right)
        
        return False