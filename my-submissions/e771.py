class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jw = set(jewels)

        counter: int = 0
        for i in stones :
            if i in jw :
                counter += 1
        
        return counter