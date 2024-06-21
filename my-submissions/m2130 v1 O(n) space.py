# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        vals = []

        while head :
            vals.append(head.val)
            head = head.next

        return max([vals[i] + vals[len(vals) - 1 - i] for i in range(ceil(len(vals) / 2))])