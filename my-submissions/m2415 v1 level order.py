# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root or not root.left :  # we are promised that every level is filled
            return root

        level = 0
        nodes = (deque(), deque())

        nodes[0].append(root.left)
        nodes[0].append(root.right)

        while nodes[level] :
            if nodes[level][0].left and nodes[level][0].left.left :
                for node in nodes[level] :
                    nodes[(level + 1) % 2].append(node.left.left)
                    nodes[(level + 1) % 2].append(node.left.right)
                    nodes[(level + 1) % 2].append(node.right.left)
                    nodes[(level + 1) % 2].append(node.right.right)

            while nodes[level] :
                nodes[level][0].val, nodes[level][-1].val = nodes[level][-1].val, nodes[level][0].val
                nodes[level].popleft()
                nodes[level].pop()

            level = (level + 1) % 2

        return root