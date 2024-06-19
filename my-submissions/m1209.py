class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []    # (letter, count)
        stkAlt = []


        for c in s :
            if stk and c == stk[-1][0] :
                stk[-1] = (c, stk[-1][1] + 1)
            else :
                stk.append((c, 1))

            if stk[-1][1] == k :
                stk.pop()


        while stk :
            c, freq = stk.pop()

            if len(stk) >= 1 and c == stk[-1][0] :   # merge
                stk[-1] = (c, stk[-1][1] + freq)
                continue
            
            if freq % k == 0 :                       # remove all substrs
                if stkAlt :
                    stk.append(stkAlt.pop())
                continue

            if freq > k :                            # remove parts above
                stk.append((c, freq % k))
                continue
            
            stkAlt.append((c, freq))
            
        stk, stkAlt = stkAlt, stk

        return ''.join([x[0] * x[1] for x in reversed(stk)])
