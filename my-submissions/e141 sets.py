# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        if not head :
            return False

        currNode = head
        while currNode.next :
            visited.add(currNode)
            currNode = currNode.next
            if currNode in visited :
                return True

        return False