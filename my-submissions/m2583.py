# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        def dfs(curr: Optional[TreeNode], dep: int = 0, sums: List[int] = []) -> List[int] :
            if not curr :
                return sums
            if dep >= len(sums) :
                sums.append(0)

            sums[dep] += curr.val

            dfs(curr.left, dep + 1, sums)
            dfs(curr.right, dep + 1, sums)

            return sums
        sums = sorted(dfs(root))
        return -1 if k > len(sums) else sums[-k]
