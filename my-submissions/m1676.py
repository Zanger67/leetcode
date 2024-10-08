# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        if not nodes :
            return None
        if len(nodes) == 1 :
            return nodes[0]

        self.commonAncestors = set()
        targetNodes = set(x.val for x in nodes)
        self.found = len(nodes)
        
        def dfs(curr: 'TreeNode', currentSet: 'Set[TreeNode]', depth: int) -> None :
            if not curr or not self.found :
                return
            currentSet.add((depth, curr))

            if curr.val in targetNodes :
                self.found -= 1
                if not self.commonAncestors :
                    for x in currentSet :
                        self.commonAncestors = currentSet.copy()
                self.commonAncestors &= currentSet
                
                # even if something's below us, none of 
                # the inbetween nodes will matter
                currentSet.remove((depth, curr))
                return
            
            dfs(curr.left, currentSet, depth + 1)
            dfs(curr.right, currentSet, depth + 1)
            currentSet.remove((depth, curr))
        
        dfs(root, set(), 0)

        depth, node = self.commonAncestors.pop()
        while self.commonAncestors :
            tempDepth, tempNode = self.commonAncestors.pop()
            if tempDepth > depth :
                depth, node = tempDepth, tempNode
        
        return node