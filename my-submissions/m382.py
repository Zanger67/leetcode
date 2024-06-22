# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

        size = 0
        curr = head
        while curr :
            curr = curr.next
            size += 1
        print(size)
        self.size = size

    def getRandom(self) -> int:
        randIndx = randint(0, self.size - 1)

        output = self.head
        for _ in range(randIndx) :
            output = output.next

        return output.val


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()