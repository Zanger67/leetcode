# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: Optional[TreeNode], p: int, q: int) -> int:
        path = [root]
        pPath = set()
        qPath = set()

        def dfs(path: List[Optional[TreeNode]],
                pPath: Set[Optional[TreeNode]],
                qPath: Set[Optional[TreeNode]]) -> None :
            if pPath and qPath :
                return

            if path[-1].val == p :
                pPath.update(path)
            if path[-1].val == q :
                qPath.update(path)

            if path[-1].left :
                path.append(path[-1].left)
                dfs(path, pPath, qPath)
                path.pop()
            if path[-1].right :
                path.append(path[-1].right)
                dfs(path, pPath, qPath)
                path.pop()

        dfs(path, pPath, qPath)

        return len(pPath) + len(qPath) - len(pPath & qPath) * 2