# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        if not head or not head.next or not head.next.next :
            return [-1, -1]

        critPts = []
        indx = 0
        prev = head.next.val
        prevprev = head.val
        head = head.next.next

        while head :
            if (prev > head.val and prev > prevprev) \
                or (prev < head.val and prev < prevprev) :
                critPts.append(indx - 1)
            prevprev = prev
            prev = head.val
            head = head.next
            indx += 1

        if len(critPts) < 2 :
            return [-1] * 2

        return [min([critPts[i] - critPts[i - 1] for i in range(1, len(critPts))]),
                critPts[-1] - critPts[0]]