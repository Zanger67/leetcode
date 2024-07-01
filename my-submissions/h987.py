# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        toVisit = deque([(0, 0, root)]) # (col, height, node)
        output = {}

        while toVisit :
            col, height, current = toVisit.popleft()
            if not current :
                continue

            if col in output :
                heapq.heappush(output[col], (height * 1000 + current.val, current.val))
            else :
                output[col] = [(height * 1000 + current.val, current.val)]

            toVisit.append((col - 1, height + 1, current.left))
            toVisit.append((col + 1, height + 1, current.right))

        return [list((y[1] for y in sorted(output.get(x)))) for x in sorted(output.keys())]