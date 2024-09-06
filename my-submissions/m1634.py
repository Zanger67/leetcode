# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        # End cases
        if not poly1 :
            return poly2
        if not poly2 :
            return poly1

        # If equal, merge
        if poly1.power == poly2.power :
            poly1.coefficient += poly2.coefficient

            # If they cancel, skip both nodes
            if poly1.coefficient == 0 :
                return self.addPoly(poly1.next, poly2.next)

            # Otherwise, merge and set next to whatever comes next recursively
            poly1.next = self.addPoly(poly1.next, poly2.next)
            return poly1

        # If one is greater, return that one and set the next to the recursion
        # If poly1 isn't the greater power, swap them
        if poly1.power < poly2.power :
            poly1, poly2 = poly2, poly1

        # Return the greater power item but replace it's next node recursively
        poly1.next = self.addPoly(poly1.next, poly2)
        return poly1
