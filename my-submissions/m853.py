# https://leetcode.com/problems/car-fleet/description/

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stk = sorted([(pos, spd) for pos, spd in zip(position, speed)], key=lambda x: abs(x[0] - target), reverse=True)

        countFleets = 1
        currPos, currSpd = stk.pop()
        timeTaken = (target - currPos) / currSpd
        longestTimeTaken = timeTaken
        while stk :
            currPos, currSpd = stk.pop()
            timeTaken = (target - currPos) / currSpd

            if (not timeTaken <= longestTimeTaken) :
                countFleets += 1
                longestTimeTaken = timeTaken
        
        return countFleets

