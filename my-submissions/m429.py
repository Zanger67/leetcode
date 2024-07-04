"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        output = []

        def dfs(curr: 'Node', depth: int = 0) -> None :
            if not curr :
                return
            if depth >= len(output) :
                output.append([])

            output[depth].append(curr.val)

            depth += 1
            for child in curr.children :
                dfs(child, depth)

        dfs(root)
        return output