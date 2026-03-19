class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        hp = []
        curr_fuel = startFuel
        curr_pos = 0
        stations_used = 0

        for pos, fuel in stations :
            curr_fuel -= (pos - curr_pos)
            curr_pos = pos
            
            while curr_fuel < 0 and hp :
                curr_fuel += -heappop(hp)
                stations_used += 1
            
            if curr_fuel < 0 :
                return -1

            heappush(hp, -fuel)
        
        curr_fuel -= (target - curr_pos)
        while curr_fuel < 0 and hp :
            curr_fuel += -heappop(hp)
            stations_used += 1
        
        if curr_fuel < 0 :
            return -1
        return stations_used
        