class Solution:
    def maxOperations(self, s: str) -> int:
        counter = 0
        onesToLeft = 0
        prev = -1

        for curr in s : 
            if curr == '1' :
                onesToLeft += 1
                prev = '1'
            elif prev == '1':
                counter += onesToLeft
                prev = '0'
            else :
                prev = '0'

        return counter