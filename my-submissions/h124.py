# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Schema: (longest independent, longestChain)
        def helper(curr: Optional[TreeNode]) -> Tuple[int, int] :
            if not curr :
                return (None, None)
            if not curr.left and not curr.right :
                return (curr.val, curr.val)

            leftInd, leftChn = helper(curr.left)
            rightInd, rightChn = helper(curr.right)

            independentCandidates = [curr.val]
            chainCandidates = [0]
            if leftInd != None :
                independentCandidates.append(leftInd)
                independentCandidates[0] += max(0, leftChn)
                chainCandidates.append(leftChn)
            if rightInd != None :
                independentCandidates.append(rightInd)
                independentCandidates[0] += max(0, rightChn)
                chainCandidates.append(rightChn)

            return (max(independentCandidates), max(chainCandidates) + curr.val)
        return max(helper(root))