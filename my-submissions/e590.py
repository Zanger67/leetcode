"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        def post(curr: 'Node', output: List[int] = []) -> List[int] :
            if not curr :
                return output
            for c in curr.children :
                post(c, output)
            output.append(curr.val)
            return output

        return post(root)
