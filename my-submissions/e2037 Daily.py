# https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum([abs(seats[x] - students[x]) for x in range(len(seats))])