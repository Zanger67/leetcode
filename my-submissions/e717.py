class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        indx = 0
        while indx <= len(bits) - 2 :
            indx += bits[indx] + 1

        return indx == len(bits) - 1