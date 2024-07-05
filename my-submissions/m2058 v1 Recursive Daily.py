# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        def helper(prevPrev: int, 
                   prev: int, 
                   curr: Optional[ListNode], 
                   output: List[int],
                   indx: int = 0) -> None :
            if (prev > curr.val and prev > prevPrev) \
                or (prev < curr.val and prev < prevPrev) :
                output.append(indx - 1)

            if curr.next :
                helper(prev, curr.val, curr.next, output, indx + 1)

        critPts = []
        if head and head.next and head.next.next :
            helper(head.val, head.next.val, head.next.next, critPts)

        if len(critPts) < 2 :
            return [-1] * 2

        return [min([critPts[i] - critPts[i - 1] for i in range(1, len(critPts))]),
                critPts[-1] - critPts[0]]