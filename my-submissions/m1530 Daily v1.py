# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        paths = []

        def dfs(paths: List[Set[TreeNode]],
                currPath: Set[TreeNode] = set([root]),
                curr: TreeNode = root) -> None :

            if not curr.left and not curr.right :
                paths.append(currPath.copy())
                return

            if curr.left :
                currPath.add(curr.left)
                dfs(paths, currPath, curr.left)
                currPath.remove(curr.left)
            if curr.right :
                currPath.add(curr.right)
                dfs(paths, currPath, curr.right)
                currPath.remove(curr.right)

        dfs(paths)

        counter = 0
        for i in range(len(paths) - 1) :
            for j in range(i + 1, len(paths)) :
                if len(paths[i]) + len(paths[j]) - len(paths[i] & paths[j]) * 2 <= distance :
                    counter += 1
        return counter