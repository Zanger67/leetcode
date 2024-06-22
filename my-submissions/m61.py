# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head :
            return None

        # Since worst case 500 nodes but  k can be much larger
        curr = head
        listLength = 0
        while curr :
            listLength += 1
            curr = curr.next

        k %= listLength

        # If rotations are redundant
        if k == 0 :
            return head


        # find k-th node from end
        beforeKth = None
        kthFromEnd = head
        for _ in range(listLength - k) :
            beforeKth = kthFromEnd
            kthFromEnd = kthFromEnd.next
        
        # kth from end is new head
        newHead = kthFromEnd
        beforeKth.next = None           # New end must not cycle
        end = kthFromEnd

        # Link end to original head
        while end.next :
            end = end.next
        
        end.next = head

        return newHead