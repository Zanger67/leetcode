# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.val = root.val
        self.stk = []

        while root :
            self.stk.append(root)
            root = root.left

    def next(self) -> int:
        curr = self.stk.pop()
        output = curr.val

        if curr.right :
            curr = curr.right
            while curr :
                self.stk.append(curr)
                curr = curr.left
        
        return output

    def hasNext(self) -> bool:
        return len(self.stk) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()