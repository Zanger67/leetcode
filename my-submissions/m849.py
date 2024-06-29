class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        maxx = 0
        indx = 0

        while not seats[indx] :
            indx += 1
        lastPerson = indx
        maxx = lastPerson
        
        for i, seat in enumerate(seats) :
            if seat :
                if maxx < (i - lastPerson) // 2 :
                    maxx = (i - lastPerson) // 2
                lastPerson = i
        
        maxx = max(maxx, len(seats) - lastPerson - 1)

        return maxx