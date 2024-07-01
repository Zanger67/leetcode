# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        depths = list(reversed([len(x) for x in re.findall('-{1,9999}', traversal)]))
        nodeVals = list(reversed([int(x) for x in re.findall('[0-9]{1,9999}', traversal)]))
        root = TreeNode(val=nodeVals.pop())

        stk = [(0, root)]
        while depths :
            depth = depths[-1]
            val = nodeVals[-1]
            peekDepth, peekNode = stk[-1]

            if depth <= peekDepth :
                stk.pop()
                continue
            
            if peekNode.left :
                peekNode.right = TreeNode(val=val)
                stk.append((depth, peekNode.right))
            else :
                peekNode.left = TreeNode(val=val)
                stk.append((depth, peekNode.left))
            depths.pop()
            nodeVals.pop()

        return root

        
