class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        seive = [False, False] + [True] * (right - 1)

        for factor in range(2, int(right ** 0.5) + 1) :
            if seive[factor] :
                for mult in range(factor ** 2, right + 1, factor) :
                    seive[mult] = False

        primes = [x for x in range(left, right + 1) if seive[x]]
        min_pair = [-1, -1]
        min_pair_dist = inf

        for x, y in zip(primes, primes[1:]) :
            if y - x < min_pair_dist :
                min_pair = [x, y]
                min_pair_dist = y - x

                if min_pair_dist == 2 :
                    break

        return min_pair