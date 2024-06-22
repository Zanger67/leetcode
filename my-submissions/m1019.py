# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        curr = head
        output = []
        size = 0
        while curr :
            output.append(curr.val)
            curr = curr.next
            size += 1

        largest = []
        for i in range(size - 1, -1, -1) :
            while largest and largest[-1] <= output[i] :
                largest.pop()
            
            if largest :
                largest.append(output[i])
                output[i] = largest[-2]
            else :
                largest.append(output[i])
                output[i] = 0
                continue

        return output