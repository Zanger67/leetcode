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

        loop: bool = False
        while currFast.next and currFast.next.next :
            currFast = currFast.next.next
            currSlow = currSlow.next

            if currFast == currSlow :
                loop = True
                break

        if not loop :
            return None

        loopSize = 1
        currFast = currFast.next
        while currFast != currSlow :
            loopSize += 1
            currFast = currFast.next
        
        currRef = head
        while True :
            for i in range(loopSize) :
                currFast = currFast.next
                if currFast == currRef :
                    return currRef
            currRef = currRef.next