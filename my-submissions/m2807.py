# https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr and curr.next :
            curr.next = ListNode(val=gcd(curr.val, curr.next.val), next=curr.next)
            curr = curr.next.next
        return head