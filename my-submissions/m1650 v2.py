# Optimized version to account for very large graphs since we don't know which one is lower
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
        visited = set()

        while True :
            if p and q :
                if p in visited :
                    return p
                visited.add(p)

                if q in visited :
                    return q
                visited.add(q)

                p = p.parent
                q = q.parent
            
            elif p :
                while p :
                    if p in visited :
                        return p
                    p = p.parent
            elif q :
                while q :
                    if q in visited :
                        return q
                    q = q.parent
            else :
                break
        
        return None


        return None