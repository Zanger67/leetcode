class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:

        flowers = [-1] * (len(bloomDay))    # flowers[i] = index of start of group
                                            # if val == -1, unused
                                            # if val < -1, -1 - val = size of grouping

        dayIndx = [(day, indx) for indx, day in enumerate(bloomDay)]
        dayIndx.sort(reverse=True)          # sorted so smallest day at top to pop

        bouquetsCollected = 0
        day = 0
        while dayIndx and bouquetsCollected < m :
            day, indx = dayIndx.pop()

            starter = indx
            if not (indx == 0 or flowers[indx - 1] == -1) :
                starter -= 1
                while flowers[starter] >= 0 :
                    starter = flowers[starter]

            if indx == starter:    # is start of group
                flowers[indx] = -2
            else :                 # to the right of a group
                flowers[indx] = starter
                bouquetsCollected -= ((-1 - flowers[starter]) // k)
                flowers[starter] -= 1

            # merge right side if exit()
            # we don't have to worry about flowers used merging
            if indx < len(flowers) - 1 and flowers[indx + 1] < -1 :
                bouquetsCollected -= ((-1 - flowers[indx + 1]) // k)  # subtract right group
                flowers[starter] += flowers[indx + 1] + 1
                flowers[indx + 1] = starter

            bouquetsCollected += (-1 - flowers[starter]) // k

        return day if m <= bouquetsCollected else -1
