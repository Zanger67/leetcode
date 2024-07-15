# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        path = [root]
        pPath = []
        qPath = []

        def dfs(path: List['TreeNode'], qPath: List['TreeNode'], pPath: List['TreeNode']) -> None :
            if qPath and pPath :
                return
            
            if path[-1] == p :
                pPath.extend(path)
            if path[-1] == q :
                qPath.extend(path)

            if path[-1].left :
                path.append(path[-1].left)
                dfs(path, qPath, pPath)
                path.pop()
            if path[-1].right :
                path.append(path[-1].right)
                dfs(path, qPath, pPath)
                path.pop()
        
        dfs(path, qPath, pPath)

        while len(qPath) < len(pPath) :
            pPath.pop()
        
        while len(qPath) > len(pPath) :
            qPath.pop()

        while qPath[-1] != pPath[-1] :
            qPath.pop()
            pPath.pop()

        return pPath[-1]