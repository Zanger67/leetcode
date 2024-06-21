# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        beforeHalf = None
        half = head
        temp = head

        # Finding halfway mark
        while temp and temp.next:
            beforeHalf = half
            half = half.next
            temp = temp.next.next

        # Reverse 2nd half
        toVisit = half
        beforeHalf.next = None
        while toVisit :
            temp = toVisit.next
            toVisit.next = beforeHalf.next
            beforeHalf.next = toVisit
            toVisit = temp
        
        maxx = 0

        left = head
        right = beforeHalf.next
        while right :
            maxx = max(maxx, left.val + right.val)
            left = left.next
            right = right.next

        return maxx