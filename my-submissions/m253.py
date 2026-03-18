class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = [x[0] for x in intervals]
        ends = [x[1] for x in intervals]

        starts.sort()
        ends.sort()

        curr_rooms = 0
        max_rooms = 0
        
        s, e = 0, 0
        while max(s, e) < len(intervals) :
            if starts[s] < ends[e] :
                curr_rooms += 1
                s += 1
                max_rooms = max(max_rooms, curr_rooms)
            else :
                curr_rooms -= 1
                e += 1
        
        return max_rooms