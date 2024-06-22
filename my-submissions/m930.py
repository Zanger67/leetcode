# Extremly similar to m1248

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        output = 0
        runningSum = 0

        prefixes = defaultdict(int)
        prefixes[0] = 1

        for num in nums :
            runningSum += num

            difference = runningSum - goal

            if difference in prefixes :
                output += prefixes[difference]
            
            prefixes[runningSum] += 1

        return output