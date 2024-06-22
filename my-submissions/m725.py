# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        listLength = 0

        curr = head
        while curr :
            curr = curr.next
            listLength += 1

        chunkSize = listLength // k
        numberOfLargerChunks = listLength - chunkSize * k
        numberOfRegularChunks = k - numberOfLargerChunks
        output = []

        prev = None
        curr = head

        while curr :
            if numberOfLargerChunks :
                numberOfLargerChunks -= 1
                currentChunkSize = chunkSize + 1

                output.append(curr)
                if prev :
                    prev.next = None
                
                for i in range(currentChunkSize) :
                    prev = curr
                    curr = curr.next
            
            elif numberOfRegularChunks :
                numberOfRegularChunks -= 1
                
                output.append(curr)
                if prev :
                    prev.next = None
                
                for i in range(chunkSize) :
                    prev = curr 
                    curr = curr.next

            else :
                break

        while numberOfRegularChunks :
            output.append(None)
            numberOfRegularChunks -= 1

        return output