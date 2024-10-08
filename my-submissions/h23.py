# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        output = ListNode()     # Dummy node
        current = output

        # heap will prioritize checking node.val -> i
        # Need i to avoid it relying on Node <= Node then causing type errors
        # i is unique
        # heap will have at most k values at any point so minimal cost for operations
        newLists = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(newLists)

        i = len(newLists)
        while newLists :
            poppedNode = heapq.heappop(newLists)[2]

            if poppedNode.next :    # if another node is found after
                i += 1
                heapq.heappush(newLists, (poppedNode.next.val, i, poppedNode.next))

            current.next = poppedNode
            current = current.next

        return output.next