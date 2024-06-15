# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        if not head.val :
            return self.removeZeroSumSublists(head.next)

        runningSums = {head.val: head, 0: None}             # key=sum   val=previousNode
        pevSum      = head.val
        current     = head.next

        while current :
            if not current.val :
                runningSums.get(pevSum).next = current.next
                return self.removeZeroSumSublists(head)

            runningSum = current.val + pevSum

            # Repeat sum found
            if runningSum in runningSums :                  # current = node right after the sequence
                previousNode = runningSums.get(runningSum)  # node before the node that starts the sequence
                if not previousNode :                       # the starting point is the head
                    return self.removeZeroSumSublists(current.next)

                previousNode.next = current.next
                return self.removeZeroSumSublists(head)

            runningSums[runningSum] = current
            current = current.next
            pevSum = runningSum

        return head