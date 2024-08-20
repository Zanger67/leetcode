class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = [[0] * len(piles) for _ in range(len(piles))]

        sfx = piles.copy()
        for i in range(2, len(piles) + 1) :
            sfx[-i] += sfx[-i + 1]

        def recurs(sfx: List[int], maxx: int, indx: int, dp: List[List[int]]) -> int :
            if indx + 2 * maxx >= len(sfx) :
                return sfx[indx]
            if dp[indx][maxx] :
                return dp[indx][maxx]

            out = inf
            for i in range(1, 2 * maxx + 1) :
                out = min(out, recurs(sfx, max(i, maxx), indx + i, dp))

            dp[indx][maxx] = sfx[indx] - out
            return dp[indx][maxx]

        return recurs(sfx, 1, 0, dp)
