# https://leetcode.com/problems/distance-between-bus-stops/

''' Notes
    A bit bulky but did it for the theoretical runtime savings. Still O(n) but 
    can save on the additional calclations if one direction is significantly
    shorter than the other by not having to have the additional addition operations.
'''

class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        counter, clockwise = start, start
        counterDist, clockwiseDist = 0, 0

        while not counter == destination and not clockwise == destination :
            counter = (counter - 1 + len(distance)) % len(distance)
            counterDist += distance[counter]

            clockwiseDist += distance[clockwise]
            clockwise = (clockwise + 1) % len(distance)

        if (clockwise == destination) :
            while not counter == destination and counterDist < clockwiseDist :
                counter = (counter - 1 + len(distance)) % len(distance)
                counterDist += distance[counter]

            if counter == destination and counterDist < clockwiseDist :
                return counterDist
            return clockwiseDist

        while not clockwise == destination and clockwiseDist < counterDist :
            clockwiseDist += distance[clockwise]
            clockwise = (clockwise + 1) % len(distance)

        if clockwise == destination and clockwiseDist < counterDist:
            return clockwiseDist
        return counterDist