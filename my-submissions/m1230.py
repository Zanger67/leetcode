class Solution:
    def probabilityOfHeads(self, prob: List[float], target: int) -> float:
        discludeRest = prob.copy()
        discludeRest[-1] = 1 - discludeRest[-1]
        for i in range(len(prob) - 2, -1, -1) :
            discludeRest[i] = discludeRest[i + 1] * (1 - prob[i])

        @cache
        def recurs(indx: int, remaining: int) -> bool :
            if indx >= len(prob) :
                if remaining :
                    return 0
                return 1

            if not remaining :
                return discludeRest[indx]

            return recurs(indx + 1, remaining - 1) * prob[indx] + \
                    recurs(indx + 1, remaining) * (1 - prob[indx])

        return recurs(0, target)