# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        hs = defaultdict(list)

        def dfs(curr: Optional[TreeNode], depth: int = 0) -> None :
            if not curr :
                return
            
            hs[depth].append(curr.val)
            
            depth += 1
            dfs(curr.left, depth)
            dfs(curr.right, depth)

        dfs(root, 0)
        print(hs)
        return [sum(hs[x]) / len(hs[x]) for x in range(1 + max(hs.keys()))]