# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        toReadd = []

        curr = head
        while curr :
            toReadd.append(curr)
            curr = curr.next

        curr = head
        numNodes = len(toReadd)
        last = head
        while numNodes > 1 :
            toReadd[-1].next = curr.next
            curr.next = toReadd.pop()
            last = curr.next
            curr = curr.next.next
            numNodes -= 2

        if numNodes == 0 :
            last.next = None
        else :
            last.next = toReadd.pop()
            last.next.next = None