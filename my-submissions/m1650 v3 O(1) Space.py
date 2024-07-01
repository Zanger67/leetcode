# O(1) SPACE ATTEMPT
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        # Find depths of each
        pDepth, qDepth = 0, 0
        curr = p
        while curr :
            pDepth += 1
            curr = curr.parent
        curr = q
        while curr :
            qDepth += 1
            curr = curr.parent

        # Make depths match and be equal
        while pDepth > qDepth :
            p = p.parent
            pDepth -= 1
        while qDepth > pDepth :
            q = q.parent
            qDepth -= 1

        # Go up till equal and output
        while p and q :
            if p == q :
                return p
            p = p.parent
            q = q.parent

        # Not connected tree
        return None