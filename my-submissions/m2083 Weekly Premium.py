# https://leetcode.com/problems/substrings-that-begin-and-end-with-the-same-letter/description/?envType=weekly-question&envId=2024-06-08

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        counter = Counter(s)
        output = len(s)

        for key in counter :
            if counter.get(key, 0) > 1 :
                output += (counter.get(key, 0)) * (counter.get(key, 0) - 1) // 2
        
        return output
