"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root :
            return root

        nodes = {}
        toVisit = [root]
        while toVisit :
            curr = toVisit.pop()
            if not curr :
                continue

            nodes[curr.val] = curr
            toVisit.append(curr.left)
            toVisit.append(curr.right)
        
        nodeVals = sorted(nodes.keys())
        output = nodes.get(nodeVals[0])
        
        for i in range(len(nodeVals)) :
            nodes[nodeVals[i]].right = nodes[nodeVals[(i + 1) % len(nodeVals)]]
            nodes[nodeVals[i]].left = nodes[nodeVals[(i - 1 + len(nodeVals)) % len(nodeVals)]]
        
        return output