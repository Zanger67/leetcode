# https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

# V2 was still using heapq which was now redundant since we sort either way at nlogn
# Though it seems it may ever so slighly be slower? Need to run side-by-side tests to confirm

class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        toVisit = deque([(0, 0, root)])     # (col, height, node)
        output = {}                         # key=col, val = (height, node.val)

        while toVisit :
            col, height, current = toVisit.popleft()
            if not current :
                continue

            if col in output :
                output[col].append((height, current.val))
            else :
                output[col] = [(height, current.val)]

            toVisit.append((col - 1, height + 1, current.left))
            toVisit.append((col + 1, height + 1, current.right))

        return [[y[1] for y in sorted(output.get(x), key=lambda l: (l[0], l[1]))] for x in sorted(output.keys())]