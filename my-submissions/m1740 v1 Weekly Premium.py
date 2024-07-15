# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        path = [root]
        pPath = []
        qPath = []

        def dfs(path: List[Optional[TreeNode]], 
                pPath: List[Optional[TreeNode]], 
                qPath: List[Optional[TreeNode]]) -> None :
            if pPath and qPath :
                return

            if path[-1].val == p :
                pPath.extend(path)
            if path[-1].val == q :
                qPath.extend(path)

            if path[-1].left :
                path.append(path[-1].left)
                dfs(path, pPath, qPath)
                path.pop()
            if path[-1].right :
                path.append(path[-1].right)
                dfs(path, pPath, qPath)
                path.pop()

        dfs(path, pPath, qPath)
        cnter = 0

        while len(pPath) < len(qPath) :
            cnter += 1
            qPath.pop()
        while len(pPath) > len(qPath) :
            cnter += 1
            pPath.pop()

        while pPath[-1] != qPath[-1] :
            cnter += 2
            pPath.pop()
            qPath.pop()

        return cnter