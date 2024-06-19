class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]

        for c in s :
            if c == '(' :
                stk.append(0)
            else :
                temp = stk.pop()
                if temp == 0 :
                    temp = 1
                else :
                    temp *= 2
                stk[-1] = stk[-1] + temp
        
        print(stk)
        return stk[-1]