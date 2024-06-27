# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        toVisit = [(root, None, 0)]       # (curr, depth)
        depths = {}

        while toVisit :
            curr, parent, depth = toVisit.pop()
            if not curr :
                continue

            if curr.left in depths or curr.right in depths :
                if parent.left == curr :
                    parent.left = None
                else :
                    parent.right = None
                break
            
            depths[curr] = depth
            depth += 1

            toVisit.append((curr.left, curr, depth))
            toVisit.append((curr.right, curr, depth))
            
        return root

