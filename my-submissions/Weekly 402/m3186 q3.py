# Did this *after* the contest finished (~1h later) with some discussion help
# Will redo later down the road once solution is no longer in my mind

class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        cnt = Counter(power)
        powerCounted = [(0, 0), (0, 0), (0, 0)] + \
                        sorted([(p, p * c) for p, c in cnt.items()], key=lambda x: x[0])

        dp = [0] * (len(powerCounted) + 3)

        def getIndexPrior(currentIndex: int) -> int :
            if powerCounted[currentIndex][0] - powerCounted[currentIndex - 1][0] > 2 :
                return currentIndex - 1
            if powerCounted[currentIndex][0] - powerCounted[currentIndex - 2][0] > 2 :
                return currentIndex - 2
            return currentIndex - 3
            
        for i in range(3, len(powerCounted)) :
            priorIndx = getIndexPrior(i)
            p, d = powerCounted[i]
            dp[i] = max(dp[priorIndx], dp[priorIndx - 1], dp[priorIndx - 2]) + d

        return max(dp)