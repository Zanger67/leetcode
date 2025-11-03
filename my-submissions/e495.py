class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        return duration + sum(min(duration, y - x) for x, y in zip(timeSeries, timeSeries[1:]))