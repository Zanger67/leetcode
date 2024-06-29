"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head :
            return None

        origNodes = {}
        newNodes  = []

        newHead = Node(head.val)

        origCurr = head
        curr = newHead

        indx = 0
        origNodes[origCurr] = indx
        newNodes.append(curr)


        while origCurr.next :
            indx += 1
            origCurr = origCurr.next
            origNodes[origCurr] = indx
            curr.next = Node(origCurr.val)
            curr = curr.next
            newNodes.append(curr)
        
        curr = newHead
        origCurr = head

        while origCurr :
            if origCurr.random :
                curr.random = newNodes[origNodes.get(origCurr.random)]
            
            origCurr = origCurr.next
            curr = curr.next
        
        return newHead
