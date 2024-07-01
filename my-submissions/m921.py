class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        brackets = []
        counter = 0
        for c in s :
            if c == '(' :
                brackets.append(True)
            elif len(brackets) > 0 and brackets[-1] :
                brackets.pop()
            else :
                counter += 1
        counter += len(brackets)
        
        return counter