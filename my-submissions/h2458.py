# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        def get_heights(curr: Optional[TreeNode], 
                        heights: dict) -> int :
            if not curr :
                return -1

            heights[curr] = 1 + max(get_heights(curr.left, heights),
                                    get_heights(curr.right, heights))
            return heights[curr]

        def set_del_heights(curr: Optional[TreeNode],
                            heights: dict,
                            del_heights: dict,
                            depth: int = 0,
                            alt_path_height: int = -1,
                            parent: Optional[TreeNode] = None) -> None :
            if not curr :
                return
            # is on _the_ or _a_ main branch causing the original root height
            if heights[root] - heights[curr] == depth :
                # root
                if not parent :
                    del_heights[curr.val] = -1
                # one child
                elif not parent.left or not parent.right :
                    del_heights[curr.val] = max(depth - 1, del_heights[parent.val])
                # two children
                else :
                    del_heights[curr.val] = max(
                        depth + heights[parent.right if parent.left == curr else parent.left],
                        alt_path_height, 
                        del_heights[parent.val])
            # non-primary path
            else :
                del_heights[curr.val] = heights[root]

            # left
            set_del_heights(curr.left,
                            heights,
                            del_heights,
                            depth + 1,
                            max(heights[curr.right] + depth + 1 if curr.right else 0,
                                alt_path_height),
                            curr)
            # right
            set_del_heights(curr.right,
                            heights,
                            del_heights,
                            depth + 1,
                            max(heights[curr.left] + depth + 1 if curr.left else 0,
                                alt_path_height),
                            curr)

        heights = {}
        get_heights(root, heights)

        del_heights = {}
        set_del_heights(root, heights, del_heights)

        return [del_heights[q] for q in queries]
