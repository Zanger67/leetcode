# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        output = []

        if k == 0 :
            output.append(target.val)
            return output

        def goingDown(curr: TreeNode) -> int :
            if not curr :
                return -1
            
            if curr == target :
                goDownK(curr.left, k - 1)
                goDownK(curr.right, k - 1)
                return k - 1
            
            left = goingDown(curr.left)
            right = goingDown(curr.right)

            if right == 0 or left == 0:
                output.append(curr.val)
                return -1
            
            if right > 0 :
                goDownK(curr.left, right - 1)
                return right - 1
            if left > 0 :
                goDownK(curr.right, left - 1)
                return left - 1

            return -1

                

        def goDownK(curr: TreeNode, kCounter: int) -> None :
            if not curr :
                return
            if not kCounter :
                output.append(curr.val)
                return
            kCounter -= 1
            goDownK(curr.left, kCounter)
            goDownK(curr.right, kCounter)

        goingDown(root)
        return output