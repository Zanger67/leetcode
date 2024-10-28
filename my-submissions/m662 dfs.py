# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(curr: Optional[TreeNode],
                lvl_maxes: List[int],
                lvl_mins: List[int],
                curr_indx: int = 0,
                depth: int = 0) -> None :
            if not curr :
                return
            
            if depth >= len(lvl_maxes) :
                lvl_maxes.append(curr_indx)
            elif curr_indx > lvl_maxes[depth] :
                lvl_maxes[depth] = curr_indx
            
            if depth >= len(lvl_mins) :
                lvl_mins.append(curr_indx)
            elif curr_indx < lvl_mins[depth] :
                lvl_maxes[depth] = curr_indx
            
            dfs(curr.left, lvl_maxes, lvl_mins, curr_indx * 2, depth + 1)
            dfs(curr.right, lvl_maxes, lvl_mins, curr_indx * 2 + 1, depth + 1)
        
        lvl_maxes = []
        lvl_mins = []
        dfs(root, lvl_maxes, lvl_mins, 0, 0)
        return max([maxx - minn + 1 for maxx, minn in zip(lvl_maxes, lvl_mins)])
