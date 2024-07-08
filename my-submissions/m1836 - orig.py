# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        cnt = defaultdict(int)
        curr = head
        while curr :
            cnt[curr.val] += 1
            curr = curr.next

        dummy = ListNode()
        dummy.next = head
        dummyHolder = dummy

        while dummy and dummy.next :
            while dummy.next and cnt[dummy.next.val] > 1 :
                dummy.next = dummy.next.next
            dummy = dummy.next
        
        return dummyHolder.next