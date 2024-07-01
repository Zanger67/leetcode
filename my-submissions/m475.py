# Only issue encountered was I assumed that the arrays were sorted :l

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        maxx = 0
        heaters.sort()
        for house in houses :
            indx = bisect_left(heaters, house)

            if indx == len(heaters): 
                maxx = max(maxx, abs(heaters[indx - 1] - house))
            elif heaters[indx] == house :
                continue
            elif indx == 0 :
                maxx = max(maxx, abs(heaters[indx] - house))
            else :
                maxx = max(maxx, min(abs(heaters[indx] - house), abs(heaters[indx - 1] - house)))

        return maxx