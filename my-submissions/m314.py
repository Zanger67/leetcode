# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = {}
        toVisit = deque([(0, root)]) # (col, node)

        while toVisit :
            col, currNode = toVisit.popleft()
            if not currNode :
                continue

            if col in output :
                output[col].append(currNode.val)
            else :
                output[col] = [currNode.val]

            toVisit.append((col + 1, currNode.left))
            toVisit.append((col - 1, currNode.right))

        return [output.get(x) for x in sorted(output.keys(), reverse=True)]
