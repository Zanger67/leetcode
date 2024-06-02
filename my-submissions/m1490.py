# https://leetcode.com/problems/clone-n-ary-tree/

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def cloneTree(self, root: 'Node') -> 'Node':
        if not root:
            return None

        children = []
        for i in root.children :
            children.append(self.cloneTree(i))
        
        return Node(root.val, children)