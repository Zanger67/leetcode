class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        dp = [startFuel] + [0] * len(stations)

        for i, (pos, fuel) in enumerate(stations) :
            for j in range(i, -1, -1) :
                if dp[j] >= pos :
                    dp[j + 1] = max(dp[j + 1], dp[j] + fuel)
        
        for i, dist in enumerate(dp) :
            if dist >= target :
                return i
        return -1