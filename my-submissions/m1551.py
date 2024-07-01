class Solution:
    def minOperations(self, n: int) -> int:
        # sum = (2 * n + 2) * n // 2
        # mean = (2 * n + 2) / 2
        # margineToMove = sum(2n+1 - ((2 * n + 2) / 2)) 
        #               = sum(2n+1 - (n+1)) 
        #               = sum(n) 
        #               = (1 + n) * n // 2
        # number of steps = margineToMove / 2 
        #                 = (1 + n) * n // 2 // 2 
        #                 = (n^2 + 1) // 4 
        #                 = n^2 // 4
        #                 = n ** 2 // 4
        return n ** 2 // 4