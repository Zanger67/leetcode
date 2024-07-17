# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        output = []

        to_delete = set(to_delete)

        # Returns pointer --> if remove then return null
        def dfs(curr: Optional[TreeNode], to_delete: set, output: List[Optional[TreeNode]]) -> Optional[TreeNode] :
            if not curr :
                return None
            
            # If found quickly, rest of traversal is redundant
            if not to_delete :
                return curr

            if curr.val in to_delete :
                to_delete.remove(curr.val)
                left = dfs(curr.left, to_delete, output)
                right = dfs(curr.right, to_delete, output)

                if left :
                    output.append(left)
                if right :
                    output.append(right)

                return None

            curr.left = dfs(curr.left, to_delete, output)
            curr.right = dfs(curr.right, to_delete, output)
            return curr

        head = dfs(root, to_delete, output)
        if head :
            output.append(head)

        return output