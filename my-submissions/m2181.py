# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next :
            if curr.next.val == 0 :
                if curr.next.next == None :
                    curr.next = None
                    break
                curr = curr.next
            else :
                curr.val += curr.next.val
                curr.next = curr.next.next
        return head