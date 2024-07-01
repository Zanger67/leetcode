# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        hp = []     # schema: (-|difference|, value)
                    # maxheap so we pop

        def dfs(curr: Optional[TreeNode], target: float, hp: list, k: int) -> None :
            if not curr :
                return
            
            absDif = -abs(target - curr.val)

            if len(hp) >= k :
                heapq.heappushpop(hp, (absDif, curr.val))
            else :
                heapq.heappush(hp, (absDif, curr.val))
            
            dfs(curr.left, target, hp, k)
            dfs(curr.right, target, hp, k)

        dfs(root, target, hp, k)
        return [x[1] for x in hp]
                