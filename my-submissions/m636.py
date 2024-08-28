class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stk = [] # schema: (functionNo, start=True/False, time)
        output = [0] * n

        # "{function_id}:{"start" | "end"}:{timestamp}"
        # e.g. "0:start:3"
        
        for log in logs :
            log = log.split(':')
            functionId = int(log[0])
            start = (log[1] == 'start')
            time = int(log[2])

            if start :
                while stk and not stk[-1] :
                    stk.pop()

                if stk :
                    output[stk[-1][0]] += time - stk[-1][2]
                stk.append([functionId, start, time])
            else : # end
                previous = stk.pop()

                while stk and stk[-1] == 0 :
                    stk.pop()

                if previous[0] == functionId : # if previous is the start of the current process
                    output[functionId] += time - previous[2] + 1
                    if stk :
                        stk[-1][2] = time + 1 # end means ending at the end of time ___
                else : # the log before isn't for the ending process
                    stk.append(previous)
                    for i in range(len(stk) - 1, -1, -1) :
                        if stk[i][0] == functionId :
                            stk[i] = 0
                            break

        return output
