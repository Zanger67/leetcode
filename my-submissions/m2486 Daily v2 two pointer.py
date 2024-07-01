# V2
# Consistently 95% memory since uses O(2) memory space lol
# 30% region for runtime

class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        pointerS, pointerT = 0, 0

        while pointerS < len(s) and pointerT < len(t) :
            if s[pointerS] == t[pointerT] :
                pointerT += 1
            pointerS += 1
        
        return len(t) - pointerT
