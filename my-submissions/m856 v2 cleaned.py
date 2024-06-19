class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = [0]

        for c in s :
            if c == '(' :
                stk.append(0)
                continue
            popped = max(1, 2 * stk.pop())
            stk[-1] += popped

        return stk[0]