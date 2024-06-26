# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
            
        currFast = head
        currSlow = head

        while currFast.next and currFast.next.next :
            currFast = currFast.next.next
            currSlow = currSlow.next

            if currFast == currSlow : # Loop found
                currSlow = head
                while currSlow != currFast :
                    currSlow = currSlow.next
                    currFast = currFast.next

                return currSlow
        return None