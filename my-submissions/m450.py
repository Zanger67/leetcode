# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(curr: Optional[TreeNode], key: int) -> Optional[TreeNode] :
            if not curr :
                return None
            if curr.val == key :
                if not curr.left :
                    return curr.right
                if not curr.left.right :
                    curr.left.right = curr.right
                    return curr.left

                predecessor = curr.left
                
                while predecessor.right and predecessor.right.right :
                    predecessor = predecessor.right
                
                curr.val = predecessor.right.val
                predecessor.right = predecessor.right.left
                
                return curr

            if curr.val < key :
                curr.right = helper(curr.right, key)
                return curr
            
            curr.left = helper(curr.left, key)
            return curr

        return helper(root, key)
