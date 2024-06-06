# https://leetcode.com/problems/hand-of-straights/description/?envType=daily-question&envId=2024-06-06

# I WAS WRONG IT'S A LOTTTT SLOWER LMAO AS IN ~10% RUNTIME AND ~30% SPACE LOL
# Still works tho 

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if groupSize == 1 or len(hand) == 0 :
            return True
        if len(hand) % groupSize :
            return False

        numCounter = Counter(hand)

        for x in range(len(hand) // groupSize):
            indx = min(numCounter.keys())
            if numCounter.get(indx) == 1 :
                numCounter.pop(indx)
            else :
                numCounter[indx] -= 1
            
            for i in range(1, groupSize) :
                if indx + i not in numCounter.keys() :
                    return False
                
                if numCounter.get(indx + i) == 1 :
                    numCounter.pop(indx + i)
                else :
                    numCounter[indx + i] -= 1

        return True