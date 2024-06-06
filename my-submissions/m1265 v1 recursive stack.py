# https://leetcode.com/problems/print-immutable-linked-list-in-reverse/
# 1 - Linear space and time complexity (due to recursive stack being linear)


# Very easy question on just datastructure understanding /shrug

# """
# This is the ImmutableListNode's API interface.
# You should not implement it, or speculate about its implementation.
# """
# class ImmutableListNode:
#     def printValue(self) -> None: # print the value of this node.
#     def getNext(self) -> 'ImmutableListNode': # return the next node.

class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        def helper(currentNode: 'ImmutableListNode') -> None:
            if (not currentNode) :
                return
            
            helper(currentNode.getNext())
            currentNode.printValue()
        
        helper(head)