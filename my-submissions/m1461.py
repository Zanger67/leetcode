class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        found = set()

        for i in range(len(s) - k + 1) :
            found.add(s[i : i + k])
        
        return len(found) == 2 ** k