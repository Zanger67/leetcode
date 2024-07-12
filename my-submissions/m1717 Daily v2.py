class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # Non-(a,b) chars act as boundaries and don't affect the final score
        chunks = re.findall('[a-b]+', s)

        # Store largest in x
        t1, t2 = 'ab', 'ba'
        if y > x :
            x, y = y, x
            t1, t2 = t2, t1

        # Parse each chunk
        output = 0
        for chk in chunks :
            rev = False
            findX = True
            findY = True
            stk = list(chk)

            # findX: check for the larger value ab/ba
            # findY: check for the smaller
            while findX or findY :
                stk2 = []
                target = t1 if findX else t2
                targetRew = x if findX else y

                while stk :
                    if not stk2 :
                        stk2.append(stk.pop())
                        continue

                    curr = stk[-1] + stk2[-1] if not rev else stk2[-1] + stk[-1]
                    if curr == target :
                        output += targetRew
                        stk.pop()
                        stk2.pop()
                        continue
                    stk2.append(stk.pop())

                if not findX :
                    break
                findX = False

                # reverse ab ba since stack appending to another stack
                # reverses the order
                rev = not rev
                stk = stk2

        return output