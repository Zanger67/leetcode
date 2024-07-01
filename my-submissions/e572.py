# A bit on the slower half of runtimes but workssss :l

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def findPotentialStarts(node: Optional[TreeNode], val) -> [] :
            if not node:
                return []
            
            output = []
            if node.val == val :
                output.append(node)
            
            return output + findPotentialStarts(node.left, val) + findPotentialStarts(node.right, val)
        
        def checkCase(node: Optional[TreeNode], subNode: Optional[TreeNode]) -> bool :
            if ((node is None) ^ (subNode is None)) :
                return False

            if not node and not subNode :
                return True

            return node.val == subNode.val and checkCase(node.left, subNode.left) and checkCase(node.right, subNode.right)

        check = findPotentialStarts(root, subRoot.val)

        for node in check :
            if checkCase(node, subRoot) :
                return True
        
        return False
