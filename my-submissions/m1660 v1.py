# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def correctBinaryTree(self, root: TreeNode) -> TreeNode:
        toVisit = [(root, 0)]       # (curr, depth)
        depths = {}

        while toVisit :
            curr, depth = toVisit.pop()
            if not curr :
                continue
            if curr in depths and depths[curr] < depth :
                continue

            depths[curr] = depth
            depth += 1

            toVisit.append((curr.left, depth))
            toVisit.append((curr.right, depth))

        toVisit.append((root))

        while toVisit :
            parent = toVisit.pop()

            if parent.left and \
                    ((parent.left.left and depths[parent.left] == depths[parent.left.left]) or \
                    (parent.left.right and depths[parent.left] == depths[parent.left.right])) :
                parent.left = None
                break

            if parent.right and \
                    ((parent.right.right and depths[parent.right] == depths[parent.right.right]) or \
                    (parent.right.left and depths[parent.right] == depths[parent.right.left])) :
                parent.right = None
                break
            
            if parent.right :
                toVisit.append(parent.right)
            if parent.left :
                toVisit.append(parent.left)


        return root

