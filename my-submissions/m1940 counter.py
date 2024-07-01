# weekly premium question

# Rank: 2

# Counts occurances of each number
# Since all values are STRICTLY increasing, repeats aren't present
# 2'd fastest it seems behind the subset method

class Solution:
    def longestCommonSubsequence(self, arrays: List[List[int]]) -> List[int]:
        counter = {}

        for subArr in arrays :
            for i in subArr :
                counter[i] = counter.get(i, 0) + 1
        
        return [x for x in counter.keys() if counter.get(x, 0) == len(arrays)]