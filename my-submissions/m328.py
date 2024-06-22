# NOTE: Requirement is O(1) space O(n) runtime

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        oddDummy = ListNode()
        oddDummyHead = oddDummy
        evenDummy = ListNode()

        curr = head
        indx = 0
        while curr :
            if indx % 2 == 0 :
                evenDummy.next = curr
                evenDummy = curr
            else :
                oddDummy.next = curr
                oddDummy = curr

            indx += 1
            curr = curr.next

        evenDummy.next = oddDummyHead.next
        oddDummy.next = None

        return head