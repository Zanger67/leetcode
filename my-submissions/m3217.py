# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, 
                     nums: List[int], 
                     head: Optional[ListNode]) -> Optional[ListNode]:
        dum = ListNode(next=head)
        dumCpy = dum
        nums = set(nums)

        while dum.next :
            if dum.next.val in nums :
                dum.next = dum.next.next
            else :
                dum = dum.next
        
        return dumCpy.next
