# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root

        def getNodeCount(curr: Optional[TreeNode]) :
            if not curr :
                return
            self.size += 1
            getNodeCount(curr.left)
            getNodeCount(curr.right)

        self.size = 0
        getNodeCount(root)

    def insert(self, val: int) -> int:
        self.size += 1
        lvl = int(log(self.size, 2))
        indx = self.size - 2 ** lvl

        path = bin(indx)
        path = (lvl - len(path) + 2) * '0' + path
        
        curr = self.root
        for direction in path[2:-1] :
            if direction == '1' :
                curr = curr.right
            else :
                curr = curr.left
        if path[-1] == '1' :
            curr.right = TreeNode(val=val)
        else :
            curr.left = TreeNode(val=val)
        return curr.val
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root
        


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()