# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        if head.next.val == head.val :
            head.next = head.next.next
            return self.deleteDuplicates(head)
        head.next = self.deleteDuplicates(head.next)
        return head
        
