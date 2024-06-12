# https://leetcode.com/problems/find-leaves-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.nodes = {0: []}

        def helper(curr: Optional[TreeNode]) -> int : # count away from leaf
            if not curr :
                return 0
            if not curr.left and not curr.right :
                self.nodes[0].append(curr.val)
                return 1
            
            maxx = max(helper(curr.left), helper(curr.right))

            if maxx in self.nodes :
                self.nodes[maxx].append(curr.val)
            else :
                self.nodes[maxx] = [curr.val]

            return maxx + 1
        
        helper(root)
        return [self.nodes[x] for x in sorted(self.nodes.keys())]
        
        # This last line could be improved to avoid a O(nlogn) worst case linked List
        # by just iterating the height / until self.nodes[x] DNE