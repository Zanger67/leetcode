# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Calculate weights of each node
        weights = defaultdict(int)

        def getWeights(curr: TreeNode) -> int :
            if not curr :
                return 0
            weight = getWeights(curr.left) + getWeights(curr.right) + 1
            weights[curr] = weight
            return weight

        getWeights(root)


        # Helper methods to get the predecessor and ancestors 
        def removeNextGreatest(curr: TreeNode) -> TreeNode :
            if curr.left and curr.left.left :
                weights[curr] -= 1
                return removeNextGreatest(curr.left)
            weights[curr] -= 1
            output = curr.left
            curr.left = output.right
            output.right = None
            return output

        def removeNextSmaller(curr: TreeNode) -> TreeNode :
            if curr.right and curr.right.right :
                weights[curr] -= 1
                return removeNextSmaller(curr.right)
            weights[curr] -= 1
            output = curr.right
            curr.right = output.left
            output.left = None
            return output


        # Recursive method to balance each node
        def balanceBSTHelper(curr: TreeNode) -> TreeNode :
            if not curr :
                return None

            if -1 <= weights[curr.left] - weights[curr.right] <= 1 :
                curr.left = balanceBSTHelper(curr.left)
                curr.right = balanceBSTHelper(curr.right)
                weights[curr] = 1 + weights[curr.left] + weights[curr.right]
                return curr
            
            if weights[curr.right] - weights[curr.left] > 0 : # right heavier
                weights[curr] -= weights[curr.right]
                if not curr.right.left :
                    newRoot = curr.right
                    newRoot.left = curr
                    curr.right = None
                    weights[newRoot] += weights[newRoot.left]
                    return balanceBSTHelper(newRoot)

                newRoot = removeNextGreatest(curr.right)
                newRoot.right = curr.right
                newRoot.left = curr
                newRoot.left.right = None
                weights[newRoot] = weights[newRoot.left] + weights[newRoot.right] + 1

                return balanceBSTHelper(newRoot)
            
            # left heavier
            weights[curr] -= weights[curr.left]
            if not curr.left.right :
                newRoot = curr.left
                newRoot.right = curr
                curr.left = None
                weights[newRoot] += weights[newRoot.right]

                return balanceBSTHelper(newRoot)

            newRoot = removeNextSmaller(curr.left)
            newRoot.left = curr.left
            newRoot.right = curr
            newRoot.right.left = None
            weights[newRoot] = weights[newRoot.left] + weights[newRoot.right] + 1
            
            return balanceBSTHelper(newRoot)

        return balanceBSTHelper(root)