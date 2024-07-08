# n^2 comes from popping being an O(n) operation for a list
# This could be improved using a deque where we keep adding the 
# popped elements until we reach a removal case.

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        curr = list(range(1, n + 1))
        indx = k - 1
        while len(curr) > 1 :
            curr.pop(indx)
            indx = (indx + k - 1) % len(curr)
        
        return curr[0]