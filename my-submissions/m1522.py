"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """

        def helper(curr: 'Node') -> tuple : # schema: (if just children, height)
            if not curr :
                return (0, 0)
            if not curr.children :
                return (1, 1)
            
            maxx = 0 # just children
            h1, h2 = 0, 0 # top 2 heights
            for child in curr.children :
                justChild, h = helper(child)

                if h > h1 :
                    h1, h2 = h, h1
                elif h > h2 :
                    h2 = h
                
                if justChild > maxx :
                    maxx = justChild
                
            return (max(h1 + h2 + 1, maxx), h1 + 1)
        
        return helper(root)[0] - 1