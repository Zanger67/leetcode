# A bit needlessly complicated, but does it's job. Might be more efficient just to
# use the max() and min() functions to initially set the 1st and 3rd maxes given the
# added operations for large datasets, but eh.

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        maxes = []

        for i in nums :
            if i in maxes :
                continue
            if len(maxes) < 3 :
                if (len(maxes) == 0) :
                    maxes.append(i)
                elif len(maxes) == 1 :
                    if i > maxes[0] :
                        maxes.append(i)
                    else :
                        maxes.insert(0, i)
                else :
                    if i > maxes[1] :
                        maxes.append(i)
                    elif i > maxes[0] :
                        maxes.insert(1, i)
                    else :
                        maxes.insert(0, i)
                continue
            
            if i > maxes[2] :
                maxes[0] = maxes[1]
                maxes[1] = maxes[2]
                maxes[2] = i
            elif i > maxes[1] :
                maxes[0] = maxes[1]
                maxes[1] = i
            elif i > maxes[0] :
                maxes[0] = i
        if len(maxes) < 3 :
            return max(maxes)
        else :
            return maxes[0]