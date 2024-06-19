class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals :
            return [newInterval]
        
        output = []
        intervals.append(newInterval)
        intervals.sort(key=lambda x : x[0], reverse=True)
        output.append(intervals.pop())

        while intervals :
            start, end = intervals.pop()

            if output[-1][1] < start :
                output.append([start, end])
            elif output[-1][1] < end :
                output[-1][1] = end
        
        return output