class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        flowers = [-1] * (len(bloomDay))    # flowers[i] = index of start of group
                                            # if val == -1, unused
                                            # if val < -1, -1 - val = size of grouping

        dayIndx = [(day, indx) for indx, day in enumerate(bloomDay)]
        dayIndx.sort(reverse=True)          # sorted so smallest day at top to pop

        def findStarter(indx: int) -> int :
            if indx == 0 or flowers[indx - 1] == -1 :
                return indx
            
            indx -= 1

            while flowers[indx] >= 0 :
                indx = flowers[indx]
            return indx

        flowersUsed = 0
        maxDay = 0
        while dayIndx and flowersUsed < m * k :
            day, indx = dayIndx.pop()
            maxDay = day
            
            starter = findStarter(indx)

            if indx == starter:    # is start of group
                flowers[indx] = -2
            else :                 # to the right of a group
                flowers[indx] = starter
                flowersUsed -= ((-1 - flowers[starter]) // k * k)
                flowers[starter] -= 1

            # merge right side if exit()
            # we don't have to worry about flowers used merging
            if indx < len(flowers) - 1 and flowers[indx + 1] < -1 :
                flowersUsed -= ((-1 - flowers[indx + 1]) // k) * k  # subtract right group
                flowers[starter] += flowers[indx + 1] + 1
                flowers[indx + 1] = starter

            flowersUsed += (-1 - flowers[starter]) // k * k

        return maxDay if k * m <= flowersUsed else -1
