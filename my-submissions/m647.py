class Solution:
    def countSubstrings(self, s: str) -> int:
        counter = 0

        for i in range(len(s)) :
            offset = 0
            while 0 <= i - offset \
                  and i + offset < len(s) \
                  and s[i - offset] == s[i + offset] :
                  offset += 1
                  counter += 1
        
        for i in range(len(s) - 1) :
            offset = 0
            while 0 <= i - offset \
                  and i + offset + 1 < len(s) \
                  and s[i - offset] == s[i + offset + 1] :
                  offset += 1
                  counter += 1

        return counter
            