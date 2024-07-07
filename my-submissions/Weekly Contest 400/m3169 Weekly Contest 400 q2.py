# https://leetcode.com/problems/count-days-without-meetings/

# Did in Weekly-Contest 400
# https://leetcode.com/contest/weekly-contest-400/

''' Notes
    days - meetingDays --> but meetingDays has overlaps
    days - meetingDays + overlaps = answer
    
'''


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings = sorted(meetings)
        
        currentL, currentR = meetings[0]
        counter = currentL - 1
        
        # print(meetings)
        for met in meetings[1:] :
            # print(currentL, currentR)
            if met[0] <= currentR :
                currentR = max(met[1], currentR)
            else :
                counter += met[0] - currentR - 1
                currentL, currentR = met
                
        # print(counter, counter?
        counter += days - currentR
        return counter