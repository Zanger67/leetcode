# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start, end = [], []

        def dfs(curr: Optional[TreeNode], start: List[str], target: List[str], path: List[str] = []) -> None :
            if start and target :
                return

            if curr.val == startValue :
                start.extend(path)
            if curr.val == destValue :
                target.extend(path)

            if curr.left :
                path.append('L')
                dfs(curr.left, start, target, path)
                path.pop()
            if curr.right :
                path.append('R')
                dfs(curr.right, start, target, path)
                path.pop()

        dfs(root, start, end)

        shorter = min(len(start), len(end))
        ups = 0
        while ups < shorter :
            if start[ups] != end[ups] :
                break
            ups += 1

        return 'U' * (len(start) - ups) + ''.join(end[ups:])