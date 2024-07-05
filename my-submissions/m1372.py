# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        goneLeft = set()
        goneRight = set()

        maxx = 0
        toVisit = [root]

        while toVisit :
            curr = toVisit.pop()
            if curr.right and curr not in goneRight :
                cnt = 0
                direction = True
                temp = curr
                while temp :
                    if direction :
                        goneRight.add(temp)
                        temp = temp.right
                    else :
                        goneLeft.add(temp)
                        temp = temp.left
                    direction = not direction
                    cnt += 1
                maxx = max(maxx, cnt - 1)
            
            if curr.left and curr not in goneLeft :
                cnt = 0
                direction = False
                temp = curr
                while temp :
                    if direction :
                        goneRight.add(temp)
                        temp = temp.right
                    else :
                        goneLeft.add(temp)
                        temp = temp.left
                    direction = not direction
                    cnt += 1
                maxx = max(maxx, cnt - 1)

            if curr.right :
                toVisit.append(curr.right)
            if curr.left :
                toVisit.append(curr.left)

        return maxx