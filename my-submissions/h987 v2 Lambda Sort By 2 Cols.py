# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        toVisit = deque([(0, 0, root)])     # (col, height, node)
        output = {}                         # key=col, val = (height, node.val)

        while toVisit :
            col, height, current = toVisit.popleft()
            if not current :
                continue

            if col in output :
                heapq.heappush(output[col], (height, current.val))
            else :
                output[col] = [(height, current.val)]

            toVisit.append((col - 1, height + 1, current.left))
            toVisit.append((col + 1, height + 1, current.right))

        return [[y[1] for y in sorted(output.get(x), key=lambda l: (l[0], l[1]))] for x in sorted(output.keys())]