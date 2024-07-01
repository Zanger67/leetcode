class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cntS, cntT = Counter(s), Counter(t)

        if not cntS == cntT :
            return False

        for key in cntS :
            if cntS.get(key) != cntT.get(key) :
                return False

        return True