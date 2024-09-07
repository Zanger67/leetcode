# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(currHead: Optional[ListNode], currNode: Optional[TreeNode]) -> bool :
            if not currHead :
                return True
            
            if not currNode :
                return False
            
            if currHead.val == currNode.val :
                return dfs(currHead.next, currNode.left) or dfs(currHead.next, currNode.right)
            return False

        def checkEach(curr: Optional[TreeNode]) -> bool :
            if not curr :
                return False
            return (curr.val == head.val and (dfs(head.next, curr.left) 
                                         or dfs(head.next, curr.right))) \
                   or checkEach(curr.left) \
                   or checkEach(curr.right)

        return checkEach(root)
