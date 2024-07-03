# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        toVisit = deque()
        toVisit.append((root, 1))

        while toVisit :
            curr, depth = toVisit.popleft()

            if curr == u :
                if not toVisit :
                    return None
                nxt, depthNxt = toVisit.popleft()
                if depthNxt == depth :
                    return nxt
            
            if curr.left :
                toVisit.append((curr.left, depth + 1))
            if curr.right :
                toVisit.append((curr.right, depth + 1))

        return None