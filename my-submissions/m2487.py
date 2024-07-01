# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        dummy.val = inf

        def helper(currentNode: Optional[ListNode]) -> Optional[ListNode()]:
            if not currentNode :
                return None
            currentNode.next = helper(currentNode.next)

            if not currentNode.next :
                return currentNode
            
            if currentNode.next.val > currentNode.val :
                return currentNode.next
            return currentNode
        
        dummy = helper(dummy)

        return dummy.next