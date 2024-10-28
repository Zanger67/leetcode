# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        nxt_nodes = deque([(root, 0, 0)])      # node, index, depth

        max_width = 0
        leftmost, rightmost = inf, -inf
        curr_depth = None
        while nxt_nodes :
            curr, indx, depth = nxt_nodes.popleft()
            if curr_depth != depth :
                max_width = max(max_width, rightmost - leftmost + 1)
                leftmost, rightmost, curr_depth = inf, -inf, depth

            if leftmost > indx :
                leftmost = indx
            if rightmost < indx :
                rightmost = indx

            if curr.left :
                nxt_nodes.append((curr.left, 2 * indx, depth + 1))
            if curr.right :
                nxt_nodes.append((curr.right, 2 * indx + 1, depth + 1))

        max_width = max(max_width, rightmost - leftmost + 1)
        return max_width
