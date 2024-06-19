class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        stk = []

        intervals.sort(key=lambda x: x[0], reverse=True)
        
        while intervals :
            start, stop = intervals.pop()

            if not stk :
                stk.append([start, stop])
                continue

            if stk[-1][1] < start :
                stk.append([start, stop])
            elif stk[-1][1] < stop :
                stk[-1][1] = stop
            

        return stk