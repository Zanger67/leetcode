class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Store largest in x
        t1, t2 = 'ab', 'ba'
        if y > x :
            x, y = y, x
            t1, t2 = t2, t1

        output = 0
        stk = list(s)

        # Parse greater value substring
        stk2 = []
        while stk :
            if not stk2 :
                stk2.append(stk.pop())
                continue

            curr = stk[-1] + stk2[-1]
            if curr == t1 :
                output += x
                stk.pop()
                stk2.pop()
                continue
            stk2.append(stk.pop())
        stk = stk2

        # Parse lower value substring
        stk2 = []
        while stk :
            if not stk2 :
                stk2.append(stk.pop())
                continue

            curr = stk2[-1] + stk[-1]
            if curr == t2 :
                output += y
                stk.pop()
                stk2.pop()
                continue
            stk2.append(stk.pop())

        return output