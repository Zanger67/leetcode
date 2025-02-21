# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:
    def dfs(self, curr: Optional[TreeNode], curr_val: int) -> None :
        if not curr :
            return

        self.vals.add(curr_val)
        self.dfs(curr.left, curr_val * 2 + 1)
        self.dfs(curr.right, curr_val * 2 + 2)

    def __init__(self, root: Optional[TreeNode]):
        self.vals = set()
        self.dfs(root, 0)

    def find(self, target: int) -> bool:
        return target in self.vals


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)