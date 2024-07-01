class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        output = list(s)
        opens = 0
        closes = 0
        for i in range(len(output)) :
            if output[i] == '(' :
                opens += 1
            elif output[i] == ')' :
                if opens > closes :
                    closes += 1
                else :
                    output[i] = ''
        
        curIndex = len(s) - 1
        while opens > closes and curIndex >= 0 :
            if output[curIndex] == '(' :
                opens -= 1
                output[curIndex] = ''
            curIndex -= 1
            
        return ''.join(output)