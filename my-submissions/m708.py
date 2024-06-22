"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if not head :
            newHead = Node(insertVal)
            newHead.next = newHead
            return newHead

        if head.next == head :
            newNode = Node(insertVal, head)
            head.next = newNode
            return head

        curr = head
        cycle = False   # Since we don't know if our entry point was past intended
        while True :
            if curr.next == head :
                cycle = True


            ''' 1. proper place
                2. largest val
                3. smallest val 
                4. cycle found 
            '''
            if (curr.val <= insertVal <= curr.next.val) or \
                (curr.val < insertVal and curr.val > curr.next.val) or \
                (insertVal < curr.next.val and curr.val > curr.next.val) or \
                cycle :
                
                newNode = Node(insertVal, curr.next)
                curr.next = newNode
                return head
            else :
                curr = curr.next

        return None