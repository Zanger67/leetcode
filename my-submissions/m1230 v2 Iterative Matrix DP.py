class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        sols = [[0] * (target + 1) for _ in range(len(prob) + 1)]
        sols[0][0] = 1

        for r in range(1, len(prob) + 1) :
            sols[r][0] = sols[r - 1][0] * (1 - prob[r - 1])
            for c in range(1, target + 1) :
                sols[r][c] = sols[r - 1][c] * (1 - prob[r - 1]) + \
                             sols[r - 1][c - 1] * prob[r - 1]

        return sols[-1][-1]