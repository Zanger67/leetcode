# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/


# Mid to slow end runtime wise possibly due to the recursive stack BUT
# is consistently 84%+ on space efficiency huh


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # output int is current index from end (starting at 1)
        def helper(currentNode: Optional[ListNode()], n: int) -> int :
            if not currentNode :
                return 1
            
            currentNo = helper(currentNode.next, n)

            if n - currentNo == -1 : # Current node = node before node to remove
                currentNode.next = currentNode.next.next
            return currentNo + 1

        # Edge cases of n == 1, len(head)
        if not head or not head.next :
            return None
        if helper(head, n) - 1 == n :
            head = head.next

        return head