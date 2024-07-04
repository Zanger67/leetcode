# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy nodes
        negativeChain = ListNode()
        negativeChainHead = negativeChain

        positiveChain = ListNode()
        positiveChainHead = positiveChain

        curr = head

        while curr :
            if curr.val < 0 :
                negativeChain.next = curr
                negativeChain = curr
            else :
                positiveChain.next = curr
                positiveChain = curr
            curr = curr.next
        positiveChain.next = None
        negativeChain.next = None
        negativeChainHead = negativeChainHead.next
        positiveChainHead = positiveChainHead.next

        # Reverse negatives
        def reverseChain(curr: Optional[ListNode], prev: Optional[ListNode]) -> Optional[ListNode] : # return new head
            output = curr
            if not curr :
                return None
            if curr.next :
                output = reverseChain(curr.next, curr)
            curr.next = prev
            return output
        
        newHead = reverseChain(negativeChainHead, None)

        curr = newHead
        while curr and curr.next :
            curr = curr.next

        if curr :
            curr.next = positiveChainHead
            return newHead
        return positiveChainHead